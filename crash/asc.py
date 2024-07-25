# import json

# # Load the JSON data
# with open('results.json', 'r') as file:
#     data = json.load(file)

# # Add "done":"no" to each item and sort the data
# sorted_data = sorted(
#     [dict(item, done="no") for item in data],
#     key=lambda x: x['num_issues'],
#     reverse=True
# )

# # Write the sorted data back to a new JSON file
# with open('sorted_results.json', 'w') as file:
#     json.dump(sorted_data, file, indent=2)

# print("Data has been updated with 'done':'no', sorted, and saved to sorted_results.json")


# import json

# # Load the JSON data
# with open('results.json', 'r') as file:
#     data = json.load(file)

# # Add "done":"no" and calculate score for each item, then sort the data
# sorted_data = sorted(
#     [dict(item, 
#           done="no", 
#           score=item['nsloc_num'] / item['num_issues'] if item['num_issues'] != 0 else float('inf'))
#      for item in data],
#     key=lambda x: x['num_issues'],
#     reverse=True
# )

# # Write the sorted data back to a new JSON file
# with open('sorted_results.json', 'w') as file:
#     json.dump(sorted_data, file, indent=2)

# print("Data has been updated with 'done':'no', score added, sorted, and saved to sorted_results.json")



# import json

# # Load the JSON data
# with open('results.json', 'r') as file:
#     data = json.load(file)

# # Add "done":"no" and calculate score for each item
# updated_data = [
#     dict(item, 
#          done="no", 
#          score=item['nsloc_num'] / item['num_issues'] if item['num_issues'] != 0 else float('inf'))
#     for item in data
# ]

# # Sort the data in ascending order based on score
# sorted_data = sorted(updated_data, key=lambda x: x['score'])

# # Write the sorted data back to a new JSON file
# with open('sorted_results.json', 'w') as file:
#     json.dump(sorted_data, file, indent=2)

# print("Data has been updated with 'done':'no', score added, sorted by score in ascending order, and saved to sorted_results.json")



import json

# Load the JSON data
with open('results.json', 'r') as file:
    data = json.load(file)

# Add "done":"no" and calculate score for each item
updated_data = [
    dict(item, 
         done="no", 
         score=item['nsloc_num'] / item['num_issues'] if item['num_issues'] != 0 else 0.0)
    for item in data
]

# Sort the data, placing 0.0 scores at the end
sorted_data = sorted(updated_data, key=lambda x: (x['score'] == 0.0, x['score']))

# Write the sorted data back to a new JSON file
with open('sorted_results.json', 'w') as file:
    json.dump(sorted_data, file, indent=2)

print("Data has been updated with 'done':'no', score added, sorted with 0.0 scores at the end, and saved to sorted_results.json")
