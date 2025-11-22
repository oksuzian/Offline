#!/usr/bin/env python3
"""
Script to generate context files for each module in the Mu2e offline framework.
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Set, Optional

def extract_module_info(module_dir: Path) -> Dict:
    """Extract information about a module from its directory structure."""
    info = {
        'name': module_dir.name,
        'type': 'unknown',
        'modules': [],
        'libraries': [],
        'dependencies': set(),
        'description': '',
        'has_fcl': False,
        'has_test': False,
        'source_files': [],
        'header_files': []
    }
    
    cmake_file = module_dir / 'CMakeLists.txt'
    if cmake_file.exists():
        with open(cmake_file, 'r') as f:
            content = f.read()
            
            # Check for library
            if 'cet_make_library' in content:
                info['type'] = 'library'
                # Extract library dependencies
                lib_match = re.search(r'LIBRARIES PUBLIC\s+(.*?)(?=\n\w|\n\)|$)', content, re.DOTALL)
                if lib_match:
                    deps = re.findall(r'Offline::(\w+)', lib_match.group(1))
                    info['dependencies'].update(deps)
            
            # Check for art modules
            module_matches = re.findall(r'cet_build_plugin\((\w+)\s+art::module', content)
            if module_matches:
                info['type'] = 'art_module' if info['type'] == 'unknown' else info['type'] + '+art_module'
                info['modules'].extend(module_matches)
                
                # Extract module dependencies
                for match in re.finditer(r'cet_build_plugin\((\w+)\s+art::module.*?LIBRARIES REG\s+(.*?)(?=\n\)|$)', content, re.DOTALL):
                    deps = re.findall(r'Offline::(\w+)', match.group(2))
                    info['dependencies'].update(deps)
    
    # Check for source files
    src_dir = module_dir / 'src'
    if src_dir.exists():
        info['source_files'] = [f.name for f in src_dir.glob('*.cc')]
        info['source_files'].extend([f.name for f in src_dir.glob('*.C')])
    
    # Check for header files
    inc_dir = module_dir / 'inc'
    if inc_dir.exists():
        info['header_files'] = [f.name for f in inc_dir.glob('*.hh')]
    
    # Check for FCL files
    fcl_dir = module_dir / 'fcl'
    if fcl_dir.exists():
        info['has_fcl'] = True
    
    # Check for test directory
    test_dir = module_dir / 'test'
    if test_dir.exists():
        info['has_test'] = True
    
    # Try to infer description from module name
    name = module_dir.name
    if 'Geom' in name:
        info['description'] = f'Geometry definitions and services for {name.replace("Geom", "")}'
    elif 'Conditions' in name:
        info['description'] = f'Conditions data and services for {name.replace("Conditions", "")}'
    elif 'Config' in name:
        info['description'] = f'Configuration classes and utilities for {name.replace("Config", "")}'
    elif 'MC' in name:
        info['description'] = f'Monte Carlo simulation components for {name.replace("MC", "")}'
    elif 'Reco' in name:
        info['description'] = f'Reconstruction algorithms and modules for {name.replace("Reco", "")}'
    elif 'DataProducts' in name:
        info['description'] = f'Data product definitions for {name.replace("DataProducts", "")}'
    elif 'Filters' in name:
        info['description'] = f'Event filtering modules for {name.replace("Filters", "")}'
    elif 'Diag' in name:
        info['description'] = f'Diagnostic and analysis tools for {name.replace("Diag", "")}'
    else:
        info['description'] = f'Module for {name} functionality'
    
    return info

def analyze_module_source(module_dir: Path, info: Dict) -> None:
    """Analyze source files to extract more detailed information."""
    src_dir = module_dir / 'src'
    if not src_dir.exists():
        return
    
    # Look for art module classes
    for src_file in src_dir.glob('*.cc'):
        try:
            with open(src_file, 'r') as f:
                content = f.read()
                
                # Check for EDAnalyzer
                if 'class' in content and 'EDAnalyzer' in content:
                    match = re.search(r'class\s+(\w+)\s*:\s*public\s+art::EDAnalyzer', content)
                    if match:
                        info['modules'].append(f"{match.group(1)} (EDAnalyzer)")
                
                # Check for EDProducer
                if 'class' in content and 'EDProducer' in content:
                    match = re.search(r'class\s+(\w+)\s*:\s*public\s+art::EDProducer', content)
                    if match:
                        info['modules'].append(f"{match.group(1)} (EDProducer)")
                
                # Check for EDFilter
                if 'class' in content and 'EDFilter' in content:
                    match = re.search(r'class\s+(\w+)\s*:\s*public\s+art::EDFilter', content)
                    if match:
                        info['modules'].append(f"{match.group(1)} (EDFilter)")
        except Exception as e:
            pass

def generate_context_file(module_dir: Path, info: Dict) -> None:
    """Generate a MODULE_CONTEXT.md file for the module."""
    context_file = module_dir / 'MODULE_CONTEXT.md'
    
    with open(context_file, 'w') as f:
        f.write(f"# {info['name']} Module Context\n\n")
        f.write(f"## Overview\n\n")
        f.write(f"{info['description']}\n\n")
        
        f.write(f"## Module Type\n\n")
        f.write(f"- **Type**: {info['type']}\n\n")
        
        if info['modules']:
            f.write(f"## Art Modules\n\n")
            for module in info['modules']:
                f.write(f"- `{module}`\n")
            f.write("\n")
        
        if info['dependencies']:
            f.write(f"## Dependencies\n\n")
            deps = sorted(info['dependencies'])
            for dep in deps:
                f.write(f"- `{dep}`\n")
            f.write("\n")
        
        if info['source_files']:
            f.write(f"## Source Files\n\n")
            f.write(f"Key source files:\n")
            for src in sorted(info['source_files'])[:10]:  # Limit to first 10
                f.write(f"- `{src}`\n")
            if len(info['source_files']) > 10:
                f.write(f"- ... and {len(info['source_files']) - 10} more\n")
            f.write("\n")
        
        if info['header_files']:
            f.write(f"## Header Files\n\n")
            f.write(f"Key header files:\n")
            for hdr in sorted(info['header_files'])[:10]:  # Limit to first 10
                f.write(f"- `{hdr}`\n")
            if len(info['header_files']) > 10:
                f.write(f"- ... and {len(info['header_files']) - 10} more\n")
            f.write("\n")
        
        f.write(f"## Structure\n\n")
        f.write(f"- Has FCL configuration files: {'Yes' if info['has_fcl'] else 'No'}\n")
        f.write(f"- Has test directory: {'Yes' if info['has_test'] else 'No'}\n")
        f.write(f"- Number of source files: {len(info['source_files'])}\n")
        f.write(f"- Number of header files: {len(info['header_files'])}\n")
        f.write("\n")
        
        f.write(f"## Notes\n\n")
        f.write(f"*This context file was auto-generated. Please update with specific details about the module's purpose and usage.*\n")

def main():
    """Main function to generate context files for all modules."""
    workspace = Path('/workspace')
    
    # Get all module directories (directories at root level, excluding special ones)
    exclude_dirs = {'.git', 'bin', 'scripts', 'fcl', 'ups', 'boost_fix', '.muse'}
    
    modules = [d for d in workspace.iterdir() 
               if d.is_dir() and d.name not in exclude_dirs]
    
    modules.sort(key=lambda x: x.name)
    
    print(f"Found {len(modules)} modules to process...")
    
    for module_dir in modules:
        print(f"Processing {module_dir.name}...")
        info = extract_module_info(module_dir)
        analyze_module_source(module_dir, info)
        generate_context_file(module_dir, info)
    
    print(f"\nGenerated context files for {len(modules)} modules.")

if __name__ == '__main__':
    main()
