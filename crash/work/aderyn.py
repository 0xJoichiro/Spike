# WIP


import subprocess
import os
import re

def extract_scope_files(readme_path):
    with open(readme_path, 'r') as file:
        content = file.read()
    
    # Find the audit scope section
    scope_section = re.search(r'# Audit scope.*?(?=\n#|\Z)', content, re.DOTALL)
    if not scope_section:
        return []
    
    # Extract file paths
    file_paths = re.findall(r'- \[.*?\]\((.*?)\)', scope_section.group())
    return [path.split('/')[-1] for path in file_paths]

readme_path = 'README.md'
scope_files = extract_scope_files(readme_path)

# Convert the list of files to a comma-separated string
path_includes = ",".join(scope_files)

print(scope_files,"scope_files")

# Construct the Aderyn command
# Construct the Aderyn command
command = [
    "aderyn",
    "wallflower-contract-v2",
    "--scope", path_includes,
    "--output", "aderyn_report.md"
]

# Add the --no-snippets option if desired
# command.append("--no-snippets")


# Run the Aderyn command
try:
    subprocess.run(command, check=True)
    print("Aderyn analysis completed successfully. Report saved as aderyn_report.md")
except subprocess.CalledProcessError as e:
    print(f"Error running Aderyn: {e}")
except FileNotFoundError:
    print("Aderyn command not found. Make sure it's installed and in your PATH.")
