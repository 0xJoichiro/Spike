import re

# Read the file content
with open('scope.txt', 'r') as file:
    content = file.read()

# Extract file names and nSLOC values
pattern = r'(\w+\.sol)\s+(\d+)'
matches = re.findall(pattern, content)

# Convert nSLOC to integers and create a list of tuples
file_data = [(name, int(nsloc)) for name, nsloc in matches]

# Sort the list based on nSLOC in ascending order
sorted_files = sorted(file_data, key=lambda x: x[1])

with open('scope.md', 'w') as output_file:
    for file_name, nsloc in sorted_files:
        output_file.write(f"{file_name}: {nsloc}\n")

print("Sorted data has been saved to scope.md")



