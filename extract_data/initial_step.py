from bs4 import BeautifulSoup
import requests
import pandas

'''HTTP Request'''
# store website in variable
website = 'https://www.remax.ro/vanzare/case/cluj?transactionType=vanzare'
# get request
response = requests.get(website)

print(f"The respone code: {response.status_code}")


'''Soap object'''

soup = BeautifulSoup(response.content, features='html.parser')
# print(soup)

update_result = str()
# result
result_container = soup.find_all('div', {'class': 'col-xs-24 col-sm-12 col-md-12 col-lg-8'})
print(len(result_container))




'''Concatenate 2 URL Parts to get absolute url'''
url_part_1 = 'https://www.remax.ro/vanzare/case/cluj'

url_part_2 = []

for item in update_result:
    for link in item.find('div', {'class': 'relative-position-image'}):
        url_part_2.append(link.find['a'].get['href'])

print(url_part_2)

