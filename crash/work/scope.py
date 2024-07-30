# import re
# import subprocess

# def extract_scope_files(readme_path):
#     with open(readme_path, 'r') as file:
#         content = file.read()
    
#     scope_section = re.search(r'# Audit scope(.*?)(?=\n#|\Z)', content, re.DOTALL)
#     if scope_section:
#         files = re.findall(r'- \[(.*?)\]', scope_section.group(1))
#         return [file.strip() for file in files]
#     return []

# def run_cloc(files):
#     command = ['cloc'] + files
#     result = subprocess.run(command, capture_output=True, text=True)
#     print(result.stdout)

# if __name__ == '__main__':
#     readme_path = 'README.md'
#     scope_files = extract_scope_files(readme_path)
    
#     print(scope_files, "scope_files")
#     if scope_files:
#         run_cloc(scope_files)
#     else:
#         print("No files found in the audit scope section.")


import re
import subprocess
import json

def extract_scope_files(readme_path):
    with open(readme_path, 'r') as file:
        content = file.read()
    
    scope_section = re.search(r'# Audit scope(.*?)(?=\n#|\Z)', content, re.DOTALL)
    if scope_section:
        files = re.findall(r'- \[(.*?)\]', scope_section.group(1))
        return [file.strip() for file in files]
    return []

def run_cloc(file):
    command = ['cloc', '--json', file]
    result = subprocess.run(command, capture_output=True, text=True)
    return json.loads(result.stdout)

def process_files(files):
    results = []
    for file in files:
        cloc_result = run_cloc(file)
        if 'SUM' in cloc_result:
            total_lines = cloc_result['SUM']['code']
            results.append((file, total_lines))
    
    return sorted(results, key=lambda x: x[1])

if __name__ == '__main__':
    readme_path = 'README.md'
    scope_files = extract_scope_files(readme_path)
    
    if scope_files:
        sorted_results = process_files(scope_files)
        for file, lines in sorted_results:
            print(f"{file}: {lines} lines")
    else:
        print("No files found in the audit scope section.")
