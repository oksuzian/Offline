#!/usr/bin/env python3
"""
Deep bug analysis - looking for subtle bugs, logic errors, and advanced issues.
"""

import re
from pathlib import Path
from collections import defaultdict

class DeepBugFinder:
    def __init__(self):
        self.bugs = []
        
    def analyze_file(self, filepath: Path):
        """Deep analysis of a file."""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
        except:
            return
        
        # Bug 1: Iterator invalidation
        self.find_iterator_invalidation(lines, filepath)
        
        # Bug 2: Off-by-one errors in loops
        self.find_off_by_one_errors(lines, filepath)
        
        # Bug 3: Incorrect loop conditions
        self.find_incorrect_loop_conditions(lines, filepath)
        
        # Bug 4: Race conditions / thread safety
        self.find_thread_safety_issues(lines, filepath)
        
        # Bug 5: Incorrect art framework usage
        self.find_art_framework_issues(lines, filepath)
        
        # Bug 6: Incorrect pointer arithmetic
        self.find_pointer_arithmetic_issues(lines, filepath)
        
        # Bug 7: Type mismatches and conversions
        self.find_type_mismatches(lines, filepath)
        
        # Bug 8: Incorrect exception handling
        self.find_exception_handling_issues(lines, filepath)
        
        # Bug 9: Incorrect use of STL containers
        self.find_stl_container_issues(lines, filepath)
        
        # Bug 10: Potential undefined behavior
        self.find_undefined_behavior(lines, filepath)
        
        # Bug 11: Logic errors in conditions
        self.find_logic_errors(lines, filepath)
        
        # Bug 12: Incorrect string handling
        self.find_string_handling_issues(lines, filepath)
        
        # Bug 13: Resource leaks (beyond memory)
        self.find_resource_leaks(lines, filepath)
        
        # Bug 14: Incorrect use of references
        self.find_reference_issues(lines, filepath)
        
        # Bug 15: Potential buffer overflows
        self.find_buffer_overflow_risks(lines, filepath)
        
    def find_iterator_invalidation(self, lines, filepath):
        """Find iterator invalidation bugs."""
        for i, line in enumerate(lines, 1):
            # Look for erase/insert/push_back while iterating
            if re.search(r'for\s*\([^)]*iterator|for\s*\([^)]*auto.*:', line):
                # Check next 50 lines for container modification
                context = '\n'.join(lines[i:min(len(lines), i+50)])
                if re.search(r'\.erase\(|\.insert\(|\.push_back\(|\.push_front\(|\.pop_back\(|\.pop_front\(', context):
                    # Check if iterator is used after modification
                    if '++' in context or '--' in context:
                        self.bugs.append({
                            'file': str(filepath),
                            'line': i,
                            'type': 'iterator_invalidation',
                            'severity': 'high',
                            'code': line.strip(),
                            'description': 'Potential iterator invalidation: container modified during iteration'
                        })
    
    def find_off_by_one_errors(self, lines, filepath):
        """Find off-by-one errors."""
        for i, line in enumerate(lines, 1):
            # Look for loop conditions that might be off-by-one
            if 'for' in line and '<=' in line:
                # Check for size()-1 patterns that might be wrong
                if re.search(r'<\s*=\s*\w+\.size\(\)\s*-\s*1', line):
                    self.bugs.append({
                        'file': str(filepath),
                        'line': i,
                        'type': 'off_by_one',
                        'severity': 'medium',
                        'code': line.strip(),
                        'description': 'Potential off-by-one error: <= size()-1 might be incorrect'
                    })
            # Look for array access with size() without -1
            if re.search(r'\[\s*\w+\.size\(\)\s*\]', line):
                self.bugs.append({
                    'file': str(filepath),
                    'line': i,
                    'type': 'off_by_one',
                    'severity': 'high',
                    'code': line.strip(),
                    'description': 'Array access with size() - likely out of bounds (should be size()-1)'
                })
    
    def find_incorrect_loop_conditions(self, lines, filepath):
        """Find incorrect loop conditions."""
        for i, line in enumerate(lines, 1):
            # Look for infinite loop conditions
            if 'while' in line or 'for' in line:
                # Check for conditions that are always true/false
                if re.search(r'while\s*\(\s*true\s*\)|while\s*\(\s*1\s*\)|for\s*\([^)]*;\s*;\s*\)', line):
                    # Check if there's a break
                    context = '\n'.join(lines[i:min(len(lines), i+100)])
                    if 'break' not in context[:500]:
                        self.bugs.append({
                            'file': str(filepath),
                            'line': i,
                            'type': 'infinite_loop',
                            'severity': 'high',
                            'code': line.strip(),
                            'description': 'Potential infinite loop without break statement'
                        })
    
    def find_thread_safety_issues(self, lines, filepath):
        """Find thread safety issues."""
        for i, line in enumerate(lines, 1):
            # Look for static variables in art modules
            if 'static' in line and ('++' in line or '--' in line or '+=' in line or '-=' in line):
                # Check if it's in an art module method
                context_before = '\n'.join(lines[max(0, i-30):i])
                if 'produce' in context_before or 'analyze' in context_before or 'filter' in context_before:
                    self.bugs.append({
                        'file': str(filepath),
                        'line': i,
                        'type': 'thread_safety',
                        'severity': 'high',
                        'code': line.strip(),
                        'description': 'Static variable modified in art module - potential race condition'
                    })
            # Look for shared mutable state
            if 'mutable' in line:
                context_before = '\n'.join(lines[max(0, i-30):i])
                if 'produce' in context_before or 'analyze' in context_before:
                    self.bugs.append({
                        'file': str(filepath),
                        'line': i,
                        'type': 'thread_safety',
                        'severity': 'medium',
                        'code': line.strip(),
                        'description': 'Mutable member variable in art module - potential thread safety issue'
                    })
    
    def find_art_framework_issues(self, lines, filepath):
        """Find incorrect art framework usage."""
        for i, line in enumerate(lines, 1):
            # Check for getHandle without isValid check
            if 'getHandle' in line and 'getValidHandle' not in line:
                # Check if result is validated
                context = '\n'.join(lines[i:min(len(lines), i+5)])
                if 'isValid()' not in context and 'if' not in context[:100]:
                    self.bugs.append({
                        'file': str(filepath),
                        'line': i,
                        'type': 'art_api_misuse',
                        'severity': 'high',
                        'code': line.strip(),
                        'description': 'getHandle() result not checked with isValid() - may dereference invalid handle'
                    })
            # Check for produces without corresponding put
            if 'produces<' in line:
                # Look for corresponding event.put
                remaining = '\n'.join(lines[i:])
                if 'event.put' not in remaining and 'e.put' not in remaining:
                    self.bugs.append({
                        'file': str(filepath),
                        'line': i,
                        'type': 'art_api_misuse',
                        'severity': 'high',
                        'code': line.strip(),
                        'description': 'produces() declared but no corresponding event.put() found'
                    })
    
    def find_pointer_arithmetic_issues(self, lines, filepath):
        """Find incorrect pointer arithmetic."""
        for i, line in enumerate(lines, 1):
            # Look for pointer arithmetic that might be wrong
            if re.search(r'\w+\s*\+\s*\d+|ptr\s*\+\s*\w+', line):
                # Check if it's array access (safer) vs raw pointer arithmetic
                if '[' not in line and ']' not in line:
                    self.bugs.append({
                        'file': str(filepath),
                        'line': i,
                        'type': 'pointer_arithmetic',
                        'severity': 'medium',
                        'code': line.strip(),
                        'description': 'Raw pointer arithmetic - verify bounds and alignment'
                    })
    
    def find_type_mismatches(self, lines, filepath):
        """Find type mismatches."""
        for i, line in enumerate(lines, 1):
            # Look for signed/unsigned comparisons
            if re.search(r'<\s*0|>\s*0|==\s*0', line):
                # Check if comparing unsigned with 0
                context_before = '\n'.join(lines[max(0, i-5):i])
                if 'unsigned' in context_before or 'size_t' in context_before:
                    if '< 0' in line:
                        self.bugs.append({
                            'file': str(filepath),
                            'line': i,
                            'type': 'type_mismatch',
                            'severity': 'medium',
                            'code': line.strip(),
                            'description': 'Comparing unsigned type with < 0 (always false)'
                        })
    
    def find_exception_handling_issues(self, lines, filepath):
        """Find exception handling issues."""
        for i, line in enumerate(lines, 1):
            # Look for catch-all without rethrow
            if re.search(r'catch\s*\(\.\.\.\s*\)|catch\s*\([^)]*\&\s*e\s*\)', line):
                # Check if exception is rethrown or logged
                context = '\n'.join(lines[i:min(len(lines), i+10)])
                if 'throw' not in context and 'LOG' not in context and 'cout' not in context:
                    self.bugs.append({
                        'file': str(filepath),
                        'line': i,
                        'type': 'exception_handling',
                        'severity': 'medium',
                        'code': line.strip(),
                        'description': 'Exception caught but not logged or rethrown - may hide errors'
                    })
    
    def find_stl_container_issues(self, lines, filepath):
        """Find STL container misuse."""
        for i, line in enumerate(lines, 1):
            # Look for map[] access that might create unwanted entries
            if re.search(r'\w+\[[^\]]+\]', line):
                # Check if it's a map and if find() was used before
                context_before = '\n'.join(lines[max(0, i-10):i])
                if 'map' in line.lower() or 'Map' in line:
                    if '.find(' not in context_before and '.count(' not in context_before:
                        self.bugs.append({
                            'file': str(filepath),
                            'line': i,
                            'type': 'stl_container_misuse',
                            'severity': 'low',
                            'code': line.strip(),
                            'description': 'Map access with [] may create unwanted default entry - consider using find() or at()'
                        })
    
    def find_undefined_behavior(self, lines, filepath):
        """Find potential undefined behavior."""
        for i, line in enumerate(lines, 1):
            # Look for sequence point violations
            if re.search(r'\+\+.*\+\+|--.*--', line):
                self.bugs.append({
                    'file': str(filepath),
                    'line': i,
                    'type': 'undefined_behavior',
                    'severity': 'high',
                    'code': line.strip(),
                    'description': 'Multiple increments/decrements on same variable - undefined behavior'
                })
            # Look for order of evaluation issues
            if re.search(r'\([^)]*\w+\+\+[^)]*\w+\+\+[^)]*\)', line):
                self.bugs.append({
                    'file': str(filepath),
                    'line': i,
                    'type': 'undefined_behavior',
                    'severity': 'high',
                    'code': line.strip(),
                    'description': 'Multiple side effects in same expression - undefined evaluation order'
                })
    
    def find_logic_errors(self, lines, filepath):
        """Find logic errors."""
        for i, line in enumerate(lines, 1):
            # Look for always true/false conditions
            if re.search(r'if\s*\(\s*\d+\s*\)|if\s*\(\s*true\s*\)|if\s*\(\s*false\s*\)', line):
                self.bugs.append({
                    'file': str(filepath),
                    'line': i,
                    'type': 'logic_error',
                    'severity': 'high',
                    'code': line.strip(),
                    'description': 'Condition always true/false - dead code or logic error'
                })
            # Look for comparisons that are always true
            if re.search(r'if\s*\(\s*\w+\s*<\s*\w+\s*&&\s*\w+\s*>\s*\w+\s*\)', line):
                # Check if same variable
                match = re.search(r'if\s*\(\s*(\w+)\s*<\s*\w+\s*&&\s*(\w+)\s*>\s*\w+\s*\)', line)
                if match and match.group(1) == match.group(2):
                    self.bugs.append({
                        'file': str(filepath),
                        'line': i,
                        'type': 'logic_error',
                        'severity': 'high',
                        'code': line.strip(),
                        'description': 'Impossible condition: variable cannot be both < and > something'
                    })
    
    def find_string_handling_issues(self, lines, filepath):
        """Find string handling issues."""
        for i, line in enumerate(lines, 1):
            # Look for strcpy/strcat without length checks
            if 'strcpy' in line or 'strcat' in line:
                self.bugs.append({
                    'file': str(filepath),
                    'line': i,
                    'type': 'string_handling',
                    'severity': 'high',
                    'code': line.strip(),
                    'description': 'strcpy/strcat used - consider strncpy/strncat or std::string for safety'
                })
            # Look for c_str() used after string modification
            if '.c_str()' in line:
                # Check if string is modified after
                context = '\n'.join(lines[i:min(len(lines), i+10)])
                if '.append(' in context or '.erase(' in context or '=' in context:
                    self.bugs.append({
                        'file': str(filepath),
                        'line': i,
                        'code': line.strip(),
                        'type': 'string_handling',
                        'severity': 'medium',
                        'description': 'c_str() used - pointer may become invalid if string is modified'
                    })
    
    def find_resource_leaks(self, lines, filepath):
        """Find resource leaks beyond memory."""
        for i, line in enumerate(lines, 1):
            # Look for file operations
            if 'fopen' in line or 'open(' in line:
                # Check for corresponding close
                remaining = '\n'.join(lines[i:])
                if 'fclose' not in remaining[:500] and 'close(' not in remaining[:500]:
                    self.bugs.append({
                        'file': str(filepath),
                        'line': i,
                        'type': 'resource_leak',
                        'severity': 'high',
                        'code': line.strip(),
                        'description': 'File opened but may not be closed'
                    })
    
    def find_reference_issues(self, lines, filepath):
        """Find reference-related issues."""
        for i, line in enumerate(lines, 1):
            # Look for returning reference to local variable
            if re.search(r'&\s*\w+\s*\([^)]*\)\s*\{', line):
                # Check if returning a reference
                func_match = re.search(r'(\w+)\s*&\s*(\w+)\s*\(', line)
                if func_match:
                    # Check if returning local variable
                    context = '\n'.join(lines[i:min(len(lines), i+50)])
                    if 'return' in context:
                        return_match = re.search(r'return\s+(\w+)', context)
                        if return_match:
                            var_name = return_match.group(1)
                            # Check if it's a local variable
                            if re.search(rf'\w+\s+{var_name}\s*[=;]', context[:context.find('return')]):
                                self.bugs.append({
                                    'file': str(filepath),
                                    'line': i,
                                    'type': 'reference_issue',
                                    'severity': 'high',
                                    'code': line.strip(),
                                    'description': f'Returning reference to local variable {var_name} - dangling reference'
                                })
    
    def find_buffer_overflow_risks(self, lines, filepath):
        """Find buffer overflow risks."""
        for i, line in enumerate(lines, 1):
            # Look for sprintf without length check
            if 'sprintf' in line:
                self.bugs.append({
                    'file': str(filepath),
                    'line': i,
                    'type': 'buffer_overflow',
                    'severity': 'high',
                    'code': line.strip(),
                    'description': 'sprintf used - consider snprintf to prevent buffer overflow'
                })
            # Look for gets()
            if 'gets(' in line:
                self.bugs.append({
                    'file': str(filepath),
                    'line': i,
                    'type': 'buffer_overflow',
                    'severity': 'critical',
                    'code': line.strip(),
                    'description': 'gets() used - always unsafe, use fgets() instead'
                })

def main():
    workspace = Path('/workspace')
    exclude_dirs = {'.git', 'bin', 'scripts', 'fcl', 'ups', 'boost_fix', '.muse'}
    
    modules = [d for d in workspace.iterdir() 
               if d.is_dir() and d.name not in exclude_dirs]
    
    finder = DeepBugFinder()
    
    print("Performing deep bug analysis...")
    
    for module_dir in sorted(modules):
        src_dir = module_dir / 'src'
        if src_dir.exists():
            for src_file in list(src_dir.glob('*.cc')) + list(src_dir.glob('*.C')):
                finder.analyze_file(src_file)
    
    # Generate report
    by_type = defaultdict(list)
    for bug in finder.bugs:
        by_type[bug['type']].append(bug)
    
    report_file = workspace / 'DEEP_BUGS_REPORT.md'
    with open(report_file, 'w') as f:
        f.write("# Deep Bug Analysis Report\n\n")
        f.write(f"Total bugs found: {len(finder.bugs)}\n\n")
        
        f.write("## Summary by Type\n\n")
        for bug_type, bugs_list in sorted(by_type.items()):
            f.write(f"- **{bug_type}**: {len(bugs_list)} occurrences\n")
        f.write("\n")
        
        f.write("## Detailed Findings\n\n")
        for bug_type, bugs_list in sorted(by_type.items()):
            f.write(f"### {bug_type} ({len(bugs_list)} occurrences)\n\n")
            for bug in bugs_list[:30]:  # Show first 30
                f.write(f"**{bug['file']}:{bug['line']}**\n")
                f.write(f"- Severity: {bug['severity']}\n")
                f.write(f"- Code: `{bug['code']}`\n")
                f.write(f"- Description: {bug['description']}\n\n")
            if len(bugs_list) > 30:
                f.write(f"... and {len(bugs_list) - 30} more\n\n")
    
    print(f"\nFound {len(finder.bugs)} deep bugs")
    print(f"Report saved to {report_file}")

if __name__ == '__main__':
    main()
