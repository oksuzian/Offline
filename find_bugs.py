#!/usr/bin/env python3
"""
Comprehensive bug-finding script for Mu2e offline framework.
Analyzes source files for common bug patterns.
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Set, Tuple
from collections import defaultdict

class BugFinder:
    def __init__(self):
        self.bugs = []
        self.module_bugs = defaultdict(list)
        
    def analyze_file(self, filepath: Path) -> List[Dict]:
        """Analyze a single source file for bugs."""
        bugs_found = []
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
        except Exception as e:
            return bugs_found
        
        # Pattern 1: Potential null pointer dereference
        # Look for pointer usage without null checks
        for i, line in enumerate(lines, 1):
            # Check for -> or * dereference after assignment without null check
            if re.search(r'\w+\s*=\s*\w+\([^)]*\)', line) and '->' in lines[min(i, len(lines)-1):min(i+5, len(lines))]:
                if 'nullptr' not in line.lower() and 'null' not in line.lower():
                    # Check if next few lines use -> without null check
                    next_lines = ''.join(lines[i:min(i+5, len(lines))])
                    if '->' in next_lines and 'if' not in next_lines[:50]:
                        bugs_found.append({
                            'type': 'potential_null_pointer',
                            'file': str(filepath),
                            'line': i,
                            'severity': 'medium',
                            'description': f'Potential null pointer dereference: pointer assigned and used without null check'
                        })
        
        # Pattern 2: Uninitialized variables
        for i, line in enumerate(lines, 1):
            # Check for variable declaration without initialization
            if re.search(r'\b(int|double|float|bool|char|unsigned)\s+\w+\s*;', line):
                var_match = re.search(r'\b(int|double|float|bool|char|unsigned)\s+(\w+)\s*;', line)
                if var_match:
                    var_name = var_match.group(2)
                    # Check if variable is used before initialization
                    next_content = '\n'.join(lines[i:min(i+20, len(lines))])
                    if re.search(rf'\b{var_name}\b', next_content):
                        if not re.search(rf'{var_name}\s*=', lines[i-1] if i > 1 else ''):
                            bugs_found.append({
                                'type': 'uninitialized_variable',
                                'file': str(filepath),
                                'line': i,
                                'severity': 'high',
                                'description': f'Variable {var_name} may be used uninitialized'
                            })
        
        # Pattern 3: Memory leaks (new without delete, or new[] without delete[])
        new_patterns = re.finditer(r'\bnew\s+(\w+)(\[[^\]]*\])?', content)
        for match in new_patterns:
            line_num = content[:match.start()].count('\n') + 1
            is_array = match.group(2) is not None
            delete_pattern = r'delete\s*(\[\s*\])?\s*' + re.escape(match.group(0).split('(')[0].strip())
            if not re.search(delete_pattern, content[match.end():]):
                bugs_found.append({
                    'type': 'memory_leak',
                    'file': str(filepath),
                    'line': line_num,
                    'severity': 'high',
                    'description': f'Potential memory leak: {match.group(0)} without corresponding delete'
                })
        
        # Pattern 4: Array bounds issues
        for i, line in enumerate(lines, 1):
            # Check for array access with variable index
            array_access = re.search(r'(\w+)\[([^\]]+)\]', line)
            if array_access:
                array_name = array_access.group(1)
                index_expr = array_access.group(2)
                # Check if index could be negative or too large
                if 'size()' not in index_expr and 'length()' not in index_expr:
                    if not re.search(rf'{array_name}\.size\(\)|{array_name}\.length\(\)', line):
                        bugs_found.append({
                            'type': 'array_bounds',
                            'file': str(filepath),
                            'line': i,
                            'severity': 'medium',
                            'description': f'Array access {array_name}[{index_expr}] without bounds check'
                        })
        
        # Pattern 5: Division by zero
        for i, line in enumerate(lines, 1):
            if '/' in line or '%' in line:
                # Check for division/modulo operations
                div_match = re.search(r'([^/]+)\s*/\s*(\w+)', line)
                mod_match = re.search(r'([^%]+)\s*%\s*(\w+)', line)
                if div_match or mod_match:
                    divisor = (div_match or mod_match).group(2)
                    # Check if divisor is checked for zero
                    context = '\n'.join(lines[max(0, i-5):min(len(lines), i+5)])
                    if not re.search(rf'{divisor}\s*!=\s*0|{divisor}\s*>\s*0|{divisor}\s*<\s*0', context):
                        bugs_found.append({
                            'type': 'division_by_zero',
                            'file': str(filepath),
                            'line': i,
                            'severity': 'high',
                            'description': f'Potential division by zero: {divisor} not checked'
                        })
        
        # Pattern 6: Use after free / dangling pointers
        for i, line in enumerate(lines, 1):
            if 'delete' in line or 'free(' in line:
                # Find pointer being deleted
                ptr_match = re.search(r'(delete|free)\s*(\w+)', line)
                if ptr_match:
                    ptr_name = ptr_match.group(2)
                    # Check if pointer is used after deletion
                    remaining = '\n'.join(lines[i:min(len(lines), i+50)])
                    if re.search(rf'\b{ptr_name}\b', remaining):
                        bugs_found.append({
                            'type': 'use_after_free',
                            'file': str(filepath),
                            'line': i,
                            'severity': 'high',
                            'description': f'Potential use after free: {ptr_name} deleted but may be used later'
                        })
        
        # Pattern 7: Missing return statement
        for i, line in enumerate(lines, 1):
            # Check for non-void function without return
            func_match = re.search(r'(\w+)\s+(\w+)\s*\([^)]*\)\s*\{', line)
            if func_match:
                return_type = func_match.group(1)
                if return_type not in ['void', 'auto'] and return_type not in ['if', 'for', 'while', 'switch']:
                    # Find function end
                    brace_count = 0
                    found_return = False
                    for j in range(i, min(len(lines), i+200)):
                        brace_count += lines[j].count('{') - lines[j].count('}')
                        if 'return' in lines[j]:
                            found_return = True
                        if brace_count < 0:
                            break
                    if not found_return and brace_count < 0:
                        bugs_found.append({
                            'type': 'missing_return',
                            'file': str(filepath),
                            'line': i,
                            'severity': 'medium',
                            'description': f'Function may be missing return statement'
                        })
        
        # Pattern 8: Integer overflow
        for i, line in enumerate(lines, 1):
            # Check for arithmetic operations that could overflow
            if re.search(r'\+\+|--|\+\s*=|-\s*=|\\*\s*=', line):
                # Look for loop counters or accumulators
                if 'for' in lines[max(0, i-3):i] or 'while' in lines[max(0, i-3):i]:
                    bugs_found.append({
                        'type': 'integer_overflow',
                        'file': str(filepath),
                        'line': i,
                        'severity': 'low',
                        'description': 'Potential integer overflow in loop'
                    })
        
        # Pattern 9: Resource leaks (file handles, etc.)
        for i, line in enumerate(lines, 1):
            if 'fopen' in line or 'open(' in line:
                # Check for corresponding close
                remaining = '\n'.join(lines[i:min(len(lines), i+100)])
                if 'fclose' not in remaining and 'close(' not in remaining:
                    bugs_found.append({
                        'type': 'resource_leak',
                        'file': str(filepath),
                        'line': i,
                        'severity': 'medium',
                        'description': 'File handle opened but may not be closed'
                    })
        
        # Pattern 10: Comparison issues
        for i, line in enumerate(lines, 1):
            # Check for assignment instead of comparison
            if re.search(r'if\s*\([^)]*=\s*[^=]', line) and '==' not in line:
                bugs_found.append({
                    'type': 'assignment_in_condition',
                    'file': str(filepath),
                    'line': i,
                    'severity': 'high',
                    'description': 'Possible assignment (=) instead of comparison (==) in condition'
                })
        
        # Pattern 11: Unused variables
        for i, line in enumerate(lines, 1):
            # Check for variable declarations that might be unused
            var_decl = re.search(r'\b(int|double|float|bool|char|unsigned|auto)\s+(\w+)\s*=', line)
            if var_decl:
                var_name = var_decl.group(2)
                # Check if variable is used
                remaining = '\n'.join(lines[i:])
                if not re.search(rf'\b{var_name}\b', remaining):
                    bugs_found.append({
                        'type': 'unused_variable',
                        'file': str(filepath),
                        'line': i,
                        'severity': 'low',
                        'description': f'Variable {var_name} declared but possibly unused'
                    })
        
        # Pattern 12: Thread safety issues
        for i, line in enumerate(lines, 1):
            if 'static' in line and ('++' in line or '--' in line or '+=' in line or '-=' in line):
                # Check if it's in a function that could be called from multiple threads
                context = '\n'.join(lines[max(0, i-20):i])
                if 'produce' in context or 'analyze' in context or 'filter' in context:
                    bugs_found.append({
                        'type': 'thread_safety',
                        'file': str(filepath),
                        'line': i,
                        'severity': 'high',
                        'description': 'Static variable modification in art module - potential thread safety issue'
                    })
        
        # Pattern 13: Missing error handling
        for i, line in enumerate(lines, 1):
            if 'getValidHandle' in line or 'getHandle' in line:
                # Check if result is checked
                next_lines = '\n'.join(lines[i:min(len(lines), i+3)])
                if 'isValid()' not in next_lines and 'if' not in next_lines:
                    bugs_found.append({
                        'type': 'missing_error_handling',
                        'file': str(filepath),
                        'line': i,
                        'severity': 'medium',
                        'description': 'getHandle/getValidHandle result not checked for validity'
                    })
        
        return bugs_found
    
    def analyze_module(self, module_dir: Path):
        """Analyze all source files in a module."""
        src_dir = module_dir / 'src'
        if not src_dir.exists():
            return
        
        for src_file in src_dir.glob('*.cc'):
            bugs = self.analyze_file(src_file)
            if bugs:
                self.module_bugs[module_dir.name].extend(bugs)
                self.bugs.extend(bugs)
        
        for src_file in src_dir.glob('*.C'):
            bugs = self.analyze_file(src_file)
            if bugs:
                self.module_bugs[module_dir.name].extend(bugs)
                self.bugs.extend(bugs)
    
    def generate_report(self, output_file: Path):
        """Generate a bug report."""
        with open(output_file, 'w') as f:
            f.write("# Bug Analysis Report\n\n")
            f.write(f"Total bugs found: {len(self.bugs)}\n\n")
            
            # Group by severity
            by_severity = defaultdict(list)
            for bug in self.bugs:
                by_severity[bug['severity']].append(bug)
            
            f.write("## Summary by Severity\n\n")
            for severity in ['high', 'medium', 'low']:
                count = len(by_severity[severity])
                f.write(f"- **{severity.upper()}**: {count} bugs\n")
            f.write("\n")
            
            # Group by type
            by_type = defaultdict(list)
            for bug in self.bugs:
                by_type[bug['type']].append(bug)
            
            f.write("## Summary by Bug Type\n\n")
            for bug_type, bugs_list in sorted(by_type.items()):
                f.write(f"- **{bug_type}**: {len(bugs_list)} occurrences\n")
            f.write("\n")
            
            # Detailed report by module
            f.write("## Detailed Report by Module\n\n")
            for module_name in sorted(self.module_bugs.keys()):
                bugs = self.module_bugs[module_name]
                if bugs:
                    f.write(f"### {module_name}\n\n")
                    f.write(f"Found {len(bugs)} potential bugs:\n\n")
                    
                    # Group by type
                    module_by_type = defaultdict(list)
                    for bug in bugs:
                        module_by_type[bug['type']].append(bug)
                    
                    for bug_type, bugs_list in sorted(module_by_type.items()):
                        f.write(f"#### {bug_type} ({len(bugs_list)} occurrences)\n\n")
                        for bug in bugs_list[:10]:  # Limit to first 10 per type
                            f.write(f"- **{bug['file']}:{bug['line']}** - {bug['description']}\n")
                        if len(bugs_list) > 10:
                            f.write(f"- ... and {len(bugs_list) - 10} more\n")
                        f.write("\n")
                    f.write("\n")

def main():
    """Main function."""
    workspace = Path('/workspace')
    exclude_dirs = {'.git', 'bin', 'scripts', 'fcl', 'ups', 'boost_fix', '.muse'}
    
    modules = [d for d in workspace.iterdir() 
               if d.is_dir() and d.name not in exclude_dirs]
    
    modules.sort(key=lambda x: x.name)
    
    finder = BugFinder()
    
    print(f"Analyzing {len(modules)} modules for bugs...")
    
    for module_dir in modules:
        print(f"Analyzing {module_dir.name}...")
        finder.analyze_module(module_dir)
    
    # Generate report
    report_file = workspace / 'BUG_REPORT.md'
    finder.generate_report(report_file)
    
    print(f"\nAnalysis complete!")
    print(f"Found {len(finder.bugs)} potential bugs")
    print(f"Report saved to {report_file}")

if __name__ == '__main__':
    main()
