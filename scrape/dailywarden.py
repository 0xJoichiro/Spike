# import requests
# from bs4 import BeautifulSoup
# import json

# # URL of the page to scrape
# url = "https://www.dailywarden.com/"

# # Send a GET request to the URL
# response = requests.get(url)

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, "html.parser")

# # Find all the contest sections
# contest_sections = soup.find_all("div", class_="contest-section")
# print(contest_sections)
# # Create a list to store contest information
# contests = []

# # Loop through each contest section and extract the information
# for section in contest_sections:
#     contest_name = section.find("h2").text.strip()
#     details = section.find("div", class_="contest-details")
#     contest_info = {"name": contest_name, "details": {}}
    
#     if details:
#         for detail in details.find_all("p"):
#             key, value = detail.text.strip().split(":", 1)
#             contest_info["details"][key.strip()] = value.strip()
    
#     contests.append(contest_info)

# # Save the contest information to a JSON file
# with open("current_contests.json", "w") as f:
#     json.dump(contests, f, indent=2)

# print("Contest information saved to current_contests.json")



import requests
from bs4 import BeautifulSoup
import json

url = "https://www.dailywarden.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

contests = []

# Find all table rows containing contest information
contest_rows = soup.find_all("tr", {"role": "row", "data-key": True})

for row in contest_rows:
    contest = {}
    cells = row.find_all("td")
    
    # Extract contest name and link
    name_cell = cells[1].find("a")
    contest["name"] = name_cell.text.strip()
    contest["link"] =  name_cell["href"]
    
    # Extract prize amount
    prize_cell = cells[2]
    prize_text = prize_cell.text.strip()
    
    # Check if the prize has been awarded
    if "Awarded" not in prize_text and "Escalation Ended" not in prize_text and "Judging" not in prize_text:
        contest["prize"] = prize_text
        
        # Extract nSLOC (number of lines of code)
        contest["nSLOC"] = cells[3].text.strip()
        
        # Add the contest to the list only if prize hasn't been awarded
        contests.append(contest)

# Save the contest information to a JSON file
with open("sherlock_contests.json", "w") as f:
    json.dump(contests, f, indent=2)


print("Contest information saved to sherlock_contests.json")
