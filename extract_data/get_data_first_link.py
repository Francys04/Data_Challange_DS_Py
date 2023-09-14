"""Get data : Address, bedrooms, sqft, year build ..."""
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from initial_step import url_join

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

# empty lists
address = []
bedrooms = []
bathrooms = []
area = []
year_built = []
parking = []
price = []

# loop through all joined links
for link in url_join:
    response = requests.get(link)

    # create soup object
    soup = BeautifulSoup(response.content, 'html.parser')

    # address
    try:
        address.append(soup.find('span', {'data-testid': 'home-details-summary-headline'}).get_text())
    except:
        address.append('')

    # bedrooms
    try:
        bedrooms.append(soup.find('li', {'data-testid': 'bed'}).get_text())
    except:
        bedrooms.append('')

    # bathrooms
    try:
        bathrooms.append(soup.find('li', {'data-testid': 'bath'}).get_text())
    except:
        bathrooms.append('')

    # area
    try:
        area.append(soup.find('li', {'data-testid': 'floor'}).get_text())
    except:
        area.append('')

    # year_built
    try:
        year_built.append(soup.find('div', string='Year Built').findNext('div').get_text())
    except:
        year_built.append('')

    # parking
    try:
        parking.append(soup.find('div', string='Parking').findNext('div').get_text())
    except:
        parking.append('')

    # price
    try:
        price.append(soup.find('h3', {'data-testid': 'on-market-price-details'}).get_text())
    except:
        price.append('')

    # create a dictionary with results
    output = {'Address': address, 'Bedrooms': bedrooms, 'Bathrooms': bathrooms, 'Area': area,
              'Year Built': year_built, 'Parking': parking, 'Price': price}

# %%
