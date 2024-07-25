# import json
# import webbrowser

# # Open and load the JSON file
# with open('sherlock_contests.json', 'r') as file:
#     contests = json.load(file)

# # Iterate over the contests
# for contest in contests:
#     contest_id = contest['contest_id']
#     url = f"https://audits.sherlock.xyz/contests/{contest_id}"
    
#     # Open the URL in the default web browser
#     webbrowser.open(url)

# print("All contest URLs have been opened.")


import json
import webbrowser
import re
from bs4 import BeautifulSoup
import requests

# Open and load the JSON file
with open('sherlock_contests.json', 'r') as file:
    contests = json.load(file)

# Create an empty list to store the results
results = []

# Iterate over the contests
for contest in contests:
    contest_id = contest['contest_id']
    url = f"https://audits.sherlock.xyz/contests/{contest_id}"
    
    # Open the URL in the default web browser
    # webbrowser.open(url)

    # Scrape data from the contest page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the scope (nSLOC)
    scope = soup.find("p", string=re.compile(r"nSLOC|TBD")).get_text(strip=True)
    print(scope)
    
    if scope == "TBD":
        nsloc_num = 0
    else:
        nsloc_num = int(scope.replace(",", "").split()[0])
    print(nsloc_num)

    # Scrape the report page
    report_url = f"https://audits.sherlock.xyz/contests/{contest_id}/report"
    report_response = requests.get(report_url)
    report_soup = BeautifulSoup(report_response.content, 'html.parser')

    # Find all the headings that start with "Issue"
    issue_headings = report_soup.find_all(lambda tag: tag.name == 'h1' and tag.text.startswith('Issue'))

    # Count the number of issue headings
    num_issues = len(issue_headings)

    print(f"Number of issues: {num_issues}")
    print(num_issues * nsloc_num)

    # Append the result to the list
    results.append({
        "contest_id": contest_id,
        "scope": scope,
        "num_issues": num_issues,
        "nsloc_num": nsloc_num,
        "rating": (0.3 * num_issues) * (nsloc_num * 0.7),
        "prize":contest['Rewards']
    })

# Save the results to a JSON file
with open("results.json", "w", encoding="utf-8") as json_file:
    json.dump(results, json_file, indent=2)

print("Results saved to results.json")
print("All contest URLs have been opened and data has been scraped.")
