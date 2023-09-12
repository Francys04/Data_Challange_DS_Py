from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import urllib.parse
import pandas as pd

# Initialize the WebDriver (you can change 'chromedriver' to your WebDriver's filename)
driver = webdriver.Chrome()
driver.get('https://www.trulia.com/CA/San_Francisco/')

html_content = driver.page_source

soup = BeautifulSoup(html_content, 'html.parser')
print(soup.text)

"""results"""
result_container = soup.find_all('li', {'class': 'sc-fc01d244-0'})
print(len(result_container))  # 42 results

"""Update Results"""
# I just want to target the elements which have the attreibute 'data-testid'
results_up = []
for r in result_container:
    if r.has_attr('data-testid'):
        results_up.append(r)
print(len(results_up))  # 40 results

"""Concatenate 2 URL Parts to get absolute URL"""
# URL first part
url_part_1 = 'https://www.trulia.com'

# Create list for URL second part
url_part_2 = []
for item in results_up:
    for link in item.find_all('div', {'data-testid': 'property-card-details'}):
        url_part_2.append(link.find('a').get('href'))
print(len(url_part_2))

# join first and second URL
url_join = []
for link_2 in url_part_2:
    url_join.append(urllib.parse.urljoin(url_part_1, link_2))
print(url_join)

driver.quit()

# %%
