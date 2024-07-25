from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import re
import json


# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Adjust based on your preferred browser

# Navigate to the URL
url = "https://audits.sherlock.xyz/contests?filter=finished"
driver.get(url)

contest_count = 0
contests_data = []

# Wait for the page to load
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="contests/"]')))

# Scroll to load all content
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(60)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Get the page source
page_source = driver.page_source

# Parse with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find all contest cards
contest_cards = soup.find_all('a', href=re.compile(r'^contests/\d+$'))

for card in contest_cards:
    contest_id = card['href'].split('/')[-1]
    title = card.find('h2', class_='text-light-500').text.strip()
    # status = card.find('span', class_=lambda x: x and 'bg-' in x).text.strip()
    # description = card.find('p', class_='text-wrap text-xs text-dark-900').text.strip()
    contest_count += 1

    
    info_divs = card.find_all('div', class_='hidden shrink-0 basis-32 flex-col items-end gap-y-1 lg:flex')
    rewards = info_divs[0].find('h2').text.strip() if info_divs else 'N/A'
    # start_date = info_divs[1].find('h2').text.strip() if len(info_divs) > 1 else 'N/A'
    # end_date = info_divs[2].find('h2').text.strip() if len(info_divs) > 2 else 'N/A'

    print(f"Contest ID: {contest_id}")
    print(f"Title: {title}")
    # print(f"Status: {status}")
    # print(f"Description: {description}")
    print(f"Rewards: {rewards}")
    # print(f"Start Date: {start_date}")
    # print(f"End Date: {end_date}")
    print("---")

    contest_data = {
        "contest_id": contest_id,
        "Title": title,
        "Rewards": rewards
    }
    contests_data.append(contest_data)


print(f"Total number of contests scraped: {contest_count}")

with open('sherlock_contests.json', 'w') as json_file:
    json.dump(contests_data, json_file, indent=2)

print(f"Total number of contests scraped: {len(contests_data)}")
print("Data saved to sherlock_contests.json")


# Close the browser
driver.quit()
