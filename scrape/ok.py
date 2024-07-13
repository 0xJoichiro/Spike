import re
import json
from bs4 import BeautifulSoup
import requests


# Open the HTML file
with open('coreadrena_source.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Regular expression pattern to match href="contests/number"
pattern = r'href="contests/(\d+)"'

# Find all matches
matches = re.findall(pattern, html_content)

i=1
# Print the matches
for match in matches:
    # print(i)
    i+=1
    # print(f'href="contests/{match}"')



print(matches)
# Convert the list to a JSON object
json_data = json.dumps(matches)

# Write the JSON data to a file
with open('contests.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print("JSON file exported successfully!")


# Load the matches from the JSON file
with open('contests.json', 'r', encoding='utf-8') as json_file:
    matches = json.load(json_file)

# Create an empty list to store the results
results = []

# Iterate over the matches
for match in matches:
    url = f"https://audits.sherlock.xyz/contests/{match}"
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the scope (nSLOC)
    scope = soup.find("p", string=re.compile(r"nSLOC|TBD")).get_text(strip=True)
    print(scope)
    
    if(scope == "TBD"):
        nsloc_num = 0
    else:
        nsloc_num = int(scope.replace(",", "").split()[0])
        print(nsloc_num)




    # scope = int(scope.split()[0])
    report_url = f"https://audits.sherlock.xyz/contests/{match}/report"
    report_response = requests.get(report_url)

    # Assuming the HTML code is stored in a variable called `html_content`
    soup = BeautifulSoup(report_response.content, 'html.parser')

    # Find all the headings that start with "Issue"
    issue_headings = soup.find_all(lambda tag: tag.name == 'h1' and tag.text.startswith('Issue'))

    # Count the number of issue headings
    num_issues = len(issue_headings)

    print(f"Number of issues: {num_issues}")

    print(num_issues*nsloc_num)




    # # Find the scope and nslooc elements
    # scope_element = soup.find("div", {"class": "scope"})
    # nslooc_element = soup.find("div", {"class": "nslooc"})

    # # Extract the text content
    # scope = scope_element.get_text(strip=True) if scope_element else ""
    # nslooc = nslooc_element.get_text(strip=True) if nslooc_element else ""

    # Append the result to the list
    results.append({
        "contest_id": match,
        "scope": scope,
        "num_issues":num_issues,
        "nsloc_num":nsloc_num,
        "rating": (0.3*num_issues)*(nsloc_num*0.7)
    })

# Save the results to a JSON file
with open("results.json", "w", encoding="utf-8") as json_file:
    json.dump(results, json_file, indent=2)

print("Results saved to results.json")



