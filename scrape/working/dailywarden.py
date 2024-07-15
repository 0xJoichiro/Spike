

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
    
    # print(cells,"cells")
    # Extract contest name and link
    name_cell = cells[1].find("a")
    contest["name"] = name_cell.text.strip()
    contest["link"] =  name_cell["href"]
    
    # if(contest["name"] == "Aloe Update"):
    #     print(cells[4])
    #     times = row.find_all('time')


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



# import requests
# from bs4 import BeautifulSoup
# import json
# from datetime import datetime

# def fetch_contest_data(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         return BeautifulSoup(response.content, "html.parser")
#     except requests.RequestException as e:
#         print(f"Error fetching data: {e}")
#         return None

# def parse_contest_row(row):
#     cells = row.find_all("td")
#     if len(cells) < 5:
#         return None

#     name_cell = cells[1].find("a")
#     prize_cell = cells[2]
#     prize_text = prize_cell.text.strip()

#     if any(status in prize_text for status in ["Awarded", "Escalation Ended", "Judging"]):
#         return None

#     # Find elements with data-key "name.4" and "name.5"
#     start_time_element = row.find('td', {'data-key': name_cell + '.4'})
#     end_time_element = row.find('td', {'data-key': name_cell + '.5'})

#     # Extract and parse the datetime information
#     start_time = start_time_element.text.strip() if start_time_element else None
#     end_time = end_time_element.text.strip() if end_time_element else None

#     # Add the times to the contest dictionary
#     # contest["start_time"] = start_time
#     # contest["end_time"] = end_time



#     # times = row.find_all('time')
#     # print(times)
#     # start_time = end_time = None
#     # if len(times) >= 2:
#     #     start_time = datetime.fromisoformat(times[0]['datetime']).isoformat()
#     #     end_time = datetime.fromisoformat(times[1]['datetime']).isoformat()

#     return {
#         "name": name_cell.text.strip(),
#         "link": name_cell["href"],
#         "prize": prize_text,
#         "nSLOC": cells[3].text.strip(),
#         "start_time": start_time,
#         "end_time": end_time
#     }

# def main():
#     url = "https://www.dailywarden.com/"
#     soup = fetch_contest_data(url)
#     if not soup:
#         return

#     contests = []
#     contest_rows = soup.find_all("tr", {"role": "row", "data-key": True})

#     for row in contest_rows:
#         contest = parse_contest_row(row)
#         if contest:
#             contests.append(contest)

#     with open("sherlock_contests.json", "w") as f:
#         json.dump(contests, f, indent=2)

#     print(f"Contest information saved to sherlock_contests.json. Total contests: {len(contests)}")

# if __name__ == "__main__":
#     main()
