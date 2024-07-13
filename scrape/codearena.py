import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://code4rena.com/audits#completed-audits"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the audit contest sections
contest_sections = soup.find_all("div", class_="contest-section")

# Loop through each contest section and extract the information
for section in contest_sections:
    # Get the contest name
    contest_name = section.find("h2").text.strip()
    print(f"Contest Name: {contest_name}")

    # Get the contest details
    details = section.find("div", class_="contest-details")
    if details:
        print("Details:")
        for detail in details.find_all("p"):
            print(detail.text.strip())

    # Get the contest links
    links = section.find_all("a")
    if links:
        print("Links:")
        for link in links:
            print(link.get("href"))

    print("-" * 80)
