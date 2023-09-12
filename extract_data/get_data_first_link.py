"""Get data : Address, bedrooms, sqft, year build ..."""
from bs4 import BeautifulSoup
from selenium import webdriver

# store first link avaliable
driver = webdriver.Chrome()
driver.get('https://www.trulia.com/p/ca/san-francisco/1100-sacramento-st-402-san-francisco-ca-94108--2177490746')

html_content = driver.page_source

soup1 = BeautifulSoup(html_content, 'html.parser')
# print(soup1.text) # html data from first link

# Adress
result_adress = soup1.find('span', {'data-testid': 'home-details-summary-headline'}).get_text()
print(result_adress)

# bedrooms
result_bedrooms = soup1.find('li', {'data-testid': 'bed'}).get_text()
print(result_bedrooms)

# bathrooms
result_bathrooms = soup1.find('li', {'data-testid': 'bath'}).get_text()
print(result_bathrooms)

# sqft
result_sqft = soup1.find('li', {'data-testid': 'floor'}).get_text()
print(result_sqft)

# Year build
result_ybuild = soup1.find('div', string='Year Build').find_next('div').get_text()
print(result_ybuild)

# Parking if it have
result_garage = soup1.find('div', string='Parking').find_next('div').get_text()
print(result_garage)

# Price
result_price = soup1.find('h3', {'data-testid': 'on-market-price-details'}).get_text()
print(result_price)

driver.quit()

# %%
