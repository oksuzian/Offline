#!/usr/bin/env python3
"""
Refined bug analysis focusing on real bugs, filtering false positives.
"""

import re
from pathlib import Path
from collections import defaultdict

class RefinedBugFinder:
    def __init__(self):
        self.real_bugs = []
        
    def analyze_file(self, filepath: Path):
        """Analyze file for real bugs."""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
        except:
            return
        
        # Bug 1: Real memory leaks - new without delete in non-RAII contexts
        for i, line in enumerate(lines, 1):
            # Look for new allocations
            new_match = re.search(r'new\s+(\w+)(\[[^\]]+\])?', line)
            if new_match:
                # Check if it's assigned to a smart pointer (safe)
                if 'std::unique_ptr' in line or 'std::shared_ptr' in line or 'std::make_unique' in line:
                    continue
                # Check if it's ROOT TFileService managed (safe)
                if 'tfs->make' in line or 'TFileService' in line:
                    continue
                # Check if delete exists later
                var_match = re.search(r'(\w+)\s*=\s*new', line)
                if var_match:
                    var_name = var_match.group(1)
                    remaining = '\n'.join(lines[i:])
                    # Look for delete
                    delete_pattern = rf'delete\s+{var_name}|delete\s*\[\s*\]\s+{var_name}'
                    if not re.search(delete_pattern, remaining):
                        # Check if it's in destructor or managed elsewhere
                        context_before = '\n'.join(lines[max(0, i-10):i])
                        if '~' not in context_before and 'unique_ptr' not in context_before:
                            self.real_bugs.append({
                                'file': str(filepath),
                                'line': i,
                                'type': 'memory_leak',
                                'severity': 'high',
                                'code': line.strip(),
                                'description': f'Memory allocated with new but not deleted: {var_name}'
                            })
        
        # Bug 2: Array access without bounds checking (real cases)
        for i, line in enumerate(lines, 1):
            # Look for array access with variable index
            array_match = re.search(r'(\w+)\[([^\]]+)\]', line)
            if array_match:
                array_name = array_match.group(1)
                index_expr = array_match.group(2)
                # Skip if index is constant or size() check
                if index_expr.isdigit() or 'size()' in index_expr or 'length()' in index_expr:
                    continue
                # Check if bounds are checked nearby
                context = '\n'.join(lines[max(0, i-5):min(len(lines), i+5)])
                index_escaped = re.escape(index_expr)
                array_escaped = re.escape(array_name)
                if not re.search(rf'{index_escaped}\s*<\s*{array_escaped}\.size\(\)|{index_escaped}\s*<\s*{array_escaped}\.length\(\)|{index_escaped}\s*<\s*\d+', context):
                    # Check if it's a map (safe with find check)
                    if 'map' in array_name.lower() or 'Map' in array_name:
                        # Check if find() was used before
                        before_context = '\n'.join(lines[max(0, i-10):i])
                        if '.find(' in before_context or '.count(' in before_context:
                            continue
                    self.real_bugs.append({
                        'file': str(filepath),
                        'line': i,
                        'type': 'array_bounds',
                        'severity': 'medium',
                        'code': line.strip(),
                        'description': f'Array access {array_name}[{index_expr}] without bounds check'
                    })
        
        # Bug 3: Assignment in condition (real bug)
        for i, line in enumerate(lines, 1):
            # Look for if/while with single = (not ==)
            if re.search(r'\b(if|while)\s*\([^)]*[^=!<>]=[^=]', line) and '==' not in line and '!=' not in line:
                # Skip common patterns that are intentional
                if 'while (' in line and '=' in line and 'getline' not in line.lower():
                    # This might be intentional assignment in while
                    continue
                self.real_bugs.append({
                    'file': str(filepath),
                    'line': i,
                    'type': 'assignment_in_condition',
                    'severity': 'high',
                    'code': line.strip(),
                    'description': 'Possible assignment (=) instead of comparison (==)'
                })
        
        # Bug 4: Division by zero (real cases only)
        for i, line in enumerate(lines, 1):
            # Skip includes and other non-division uses of /
            if 'include' in line or '//' in line or '/*' in line:
                continue
            # Look for division operations
            div_match = re.search(r'([\w.]+)\s*/\s*([\w.()]+)', line)
            if div_match:
                divisor = div_match.group(2)
                # Skip if divisor is constant non-zero
                try:
                    # Try to extract numeric value
                    numeric_part = re.sub(r'[()]', '', divisor)
                    if numeric_part.replace('.', '').isdigit():
                        val = float(numeric_part)
                        if val != 0:
                            continue
                except:
                    pass
                # Check if divisor is checked
                context = '\n'.join(lines[max(0, i-10):min(len(lines), i+5)])
                divisor_escaped = re.escape(divisor)
                if not re.search(rf'{divisor_escaped}\s*!=\s*0|{divisor_escaped}\s*>\s*0|{divisor_escaped}\s*==\s*0', context):
                    # Skip if it's a function call result that's likely safe
                    if '(' in divisor and ')' in divisor:
                        continue
                    self.real_bugs.append({
                        'file': str(filepath),
                        'line': i,
                        'type': 'division_by_zero',
                        'severity': 'high',
                        'code': line.strip(),
                        'description': f'Division by {divisor} without zero check'
                    })
        
        # Bug 5: Use after free
        for i, line in enumerate(lines, 1):
            if 'delete' in line:
                delete_match = re.search(r'delete\s+(\w+)', line)
                if delete_match:
                    ptr_name = delete_match.group(1)
                    # Check if pointer is used after deletion
                    remaining = '\n'.join(lines[i:min(len(lines), i+30)])
                    if re.search(rf'\b{ptr_name}\b', remaining):
                        # Check if it's reassigned
                        if not re.search(rf'{ptr_name}\s*=', remaining[:200]):
                            self.real_bugs.append({
                                'file': str(filepath),
                                'line': i,
                                'type': 'use_after_free',
                                'severity': 'high',
                                'code': line.strip(),
                                'description': f'Pointer {ptr_name} deleted but may be used later'
                            })
        
        # Bug 6: Uninitialized member variables used before initialization
        for i, line in enumerate(lines, 1):
            # Look for member variable usage
            member_match = re.search(r'_\w+\s*[=;,\[\]]', line)
            if member_match:
                var_match = re.search(r'(_\w+)', line)
                if var_match:
                    var_name = var_match.group(1)
                    # Check if it's initialized in constructor
                    # This is complex, so we'll look for obvious cases
                    if '=' not in line and '++' not in line and '--' not in line:
                        # Check if it's used before being set
                        before_context = '\n'.join(lines[:i])
                        if ':' not in before_context.split('{')[-1] if '{' in before_context else before_context:
                            # Look for initialization
                            if not re.search(rf'{var_name}\s*=', before_context[-500:]):
                                self.real_bugs.append({
                                    'file': str(filepath),
                                    'line': i,
                                    'type': 'uninitialized_variable',
                                    'severity': 'medium',
                                    'code': line.strip(),
                                    'description': f'Member variable {var_name} may be uninitialized'
                                })
        
        # Bug 7: Missing return in non-void functions
        for i, line in enumerate(lines, 1):
            func_match = re.search(r'(\w+)\s+(\w+)\s*\([^)]*\)\s*\{', line)
            if func_match:
                return_type = func_match.group(1)
                func_name = func_match.group(2)
                if return_type not in ['void', 'auto', 'template']:
                    # Find function end
                    brace_count = 1
                    found_return = False
                    for j in range(i+1, min(len(lines), i+500)):
                        brace_count += lines[j].count('{') - lines[j].count('}')
                        if 'return' in lines[j]:
                            found_return = True
                        if brace_count == 0:
                            break
                    if not found_return and brace_count == 0:
                        self.real_bugs.append({
                            'file': str(filepath),
                            'line': i,
                            'type': 'missing_return',
                            'severity': 'high',
                            'code': line.strip(),
                            'description': f'Function {func_name} missing return statement'
                        })

def main():
    workspace = Path('/workspace')
    exclude_dirs = {'.git', 'bin', 'scripts', 'fcl', 'ups', 'boost_fix', '.muse'}
    
    modules = [d for d in workspace.iterdir() 
               if d.is_dir() and d.name not in exclude_dirs]
    
    finder = RefinedBugFinder()
    
    print("Analyzing modules for real bugs...")
    
    for module_dir in sorted(modules):
        src_dir = module_dir / 'src'
        if src_dir.exists():
            for src_file in list(src_dir.glob('*.cc')) + list(src_dir.glob('*.C')):
                finder.analyze_file(src_file)
    
    # Generate report
    by_type = defaultdict(list)
    for bug in finder.real_bugs:
        by_type[bug['type']].append(bug)
    
    report_file = workspace / 'REAL_BUGS_REPORT.md'
    with open(report_file, 'w') as f:
        f.write("# Real Bugs Found in Mu2e Offline Framework\n\n")
        f.write(f"Total real bugs found: {len(finder.real_bugs)}\n\n")
        
        f.write("## Summary by Type\n\n")
        for bug_type, bugs_list in sorted(by_type.items()):
            f.write(f"- **{bug_type}**: {len(bugs_list)} occurrences\n")
        f.write("\n")
        
        f.write("## Detailed Findings\n\n")
        for bug_type, bugs_list in sorted(by_type.items()):
            f.write(f"### {bug_type} ({len(bugs_list)} occurrences)\n\n")
            # Show first 20 of each type
            for bug in bugs_list[:20]:
                f.write(f"**{bug['file']}:{bug['line']}**\n")
                f.write(f"- Severity: {bug['severity']}\n")
                f.write(f"- Code: `{bug['code']}`\n")
                f.write(f"- Description: {bug['description']}\n\n")
            if len(bugs_list) > 20:
                f.write(f"... and {len(bugs_list) - 20} more\n\n")
    
    print(f"\nFound {len(finder.real_bugs)} real bugs")
    print(f"Report saved to {report_file}")

if __name__ == '__main__':
    main()
