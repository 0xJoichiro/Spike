# import requests
# from bs4 import BeautifulSoup

# def scrape_immunefi_scope(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Look for headers that might contain 'Scope'
#     scope_header = soup.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'], string=lambda text: 'scope' in text.lower() if text else False)
    
#     if scope_header:
#         scope_section = scope_header.find_next('div')
#         scope_info = scope_section.get_text(strip=True, separator='\n')
#         return scope_info
#     else:
#         return "Scope section not found"

# # Rest of the code remains the same

# # URL to scrape
# # url = "https://immunefi.com/boost/folksfinance-boost/"

# # Scrape the scope information
# scope_info = scrape_immunefi_scope("https://immunefi.com/boost/folksfinance-boost/")

# # Print the extracted information
# print(scope_info)


# import json
# import requests
# from bs4 import BeautifulSoup

# def scrape_immunefi_scope(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     scope_header = soup.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'], string=lambda text: 'scope' in text.lower() if text else False)
    
#     if scope_header:
#         scope_section = scope_header.find_next('div')
#         scope_info = scope_section.get_text(strip=True, separator='\n')
#         return scope_info
#     else:
#         return "Scope section not found"

# url = "https://immunefi.com/boost/folksfinance-boost/"
# scope_info = scrape_immunefi_scope(url)

# # Create a dictionary with the scraped information
# data = {
#     "url": url,
#     "scope_info": scope_info
# }

# # Export to JSON file
# with open('immunefi_scope.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)

# print("Scope information has been exported to immunefi_scope.json")


import requests
from bs4 import BeautifulSoup

def scrape_immunefi_scope(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    scope_header = soup.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'], string=lambda text: 'scope' in text.lower() if text else False)
    
    if scope_header:
        scope_section = scope_header.find_next('div')
        scope_info = scope_section.get_text(strip=True, separator='\n')
        return scope_info
    else:
        return "Scope section not found"

url = "https://immunefi.com/boost/folksfinance-boost/"
scope_info = scrape_immunefi_scope(url)

# Export to text file
with open('immunefi_scope.txt', 'w') as txt_file:
    txt_file.write(f"URL: {url}\n\n")
    txt_file.write("Scope Information:\n")
    txt_file.write(scope_info)

print("Scope information has been exported to immunefi_scope.txt")
