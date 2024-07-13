# import requests
# from bs4 import BeautifulSoup

# def scrape_boosts():
#     url = "https://immunefi.com/boost/"  # Replace with the actual URL
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     boosts = soup.find_all('div', class_='p-[3px] text-white md:space-y-8 rounded bg-gradient-to-b from-[#50FF24] to-[#25FBA1]')

#     for boost in boosts:
#         name = boost.find('div', class_='font-medium').text.strip()
#         reward = boost.find('div', string='Rewards up to').find_next('div').text.strip()
#         status = boost.find('span', class_='text-[#51FF25]').text.strip()
#         time_remaining = boost.find('div', class_='mt-1 text-[14px] font-normal').text.strip()

#         print(f"Name: {name}")
#         print(f"Reward: {reward}")
#         print(f"Status: {status}")
#         print(f"Time Remaining: {time_remaining}")
#         print("---")

# if __name__ == "__main__":
#     scrape_boosts()



import requests
from bs4 import BeautifulSoup

def scrape_boost_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract detailed information from the individual boost page
    # This is a placeholder - you'll need to adjust based on the actual page structure
    details = soup.find('div', class_='boost-details')
    if details:
        return details.text.strip()
    return "No additional details found"

def scrape_boosts():
    url = "https://immunefi.com/boost/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    boosts = soup.find_all('div', class_='p-[3px] text-white md:space-y-8 rounded bg-gradient-to-b from-[#50FF24] to-[#25FBA1]')

    print(boosts)
    for boost in boosts:
        # name = boost.find('div', class_='font-medium').text.strip()
        # reward = boost.find('div', string='Rewards up to').find_next('div').text.strip()
        # status = boost.find('span', class_='text-[#51FF25]').text.strip()
        # time_remaining = boost.find('div', class_='mt-1 text-[14px] font-normal').text.strip()
        
        # Find and follow the link to the individual boost page
        link = boost.find('a', class_='btn')['href']
        print(f"Link: {link}")
        full_link = f"https://immunefi.com{link}"
        
        additional_details = scrape_boost_details(full_link)

        print(f"Name: {name}")
        print(f"Reward: {reward}")
        print(f"Status: {status}")
        print(f"Time Remaining: {time_remaining}")
        print(f"Additional Details: {additional_details}")
        print("---")

if __name__ == "__main__":
    scrape_boosts()
