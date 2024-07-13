# import json

# # Load the data from the JSON file
# with open('results.json', 'r') as file:
#     data = json.load(file)

# # Sort the list of dictionaries by the 'rating' value in ascending order
# sorted_data = sorted(data, key=lambda x: x['rating'])

# # Save the sorted data to a new JSON file
# with open('sorted_results.json', 'w') as file:
#     json.dump(sorted_data, file, indent=2)

# print("Sorted data saved to 'sorted_results.json'")


# import json

# # Load the JSON data from the file
# with open('sorted_results.json', 'r') as file:
#     data = json.load(file)

# # Iterate over the list and add the "status" key-value pair
# for item in data:
#     item['status'] = "No"

# # Save the modified data back to the file
# with open('sorted_results.json', 'w') as file:
#     json.dump(data, file, indent=2)



import json

# Load the data from the JSON file
with open('sorted_results.json', 'r') as file:
    data = json.load(file)

# Sort the list of dictionaries by the 'num_issues' value in ascending order
sorted_data = sorted(data, key=lambda x: x['num_issues'])

# Save the sorted data to a new JSON file
with open('sorted_by_issues.json', 'w') as file:
    json.dump(sorted_data, file, indent=2)

print("Sorted data saved to 'sorted_by_issues.json'")
