import requests
from bs4 import BeautifulSoup

from const import URL

response = requests.get(URL)

# Перевіряємо доступ до сайту
# print(response)
# print(response.text)

soup = BeautifulSoup(response.text, "lxml") #html.parser
# print(soup)

data = soup.find("div",class_="w-full rounded border")
name = data.find('h4').text.replace("\n","")
price = data.find('h5').text.replace("$","")

print(name)
print(price)
