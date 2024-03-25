import requests
from bs4 import BeautifulSoup
from time import sleep
from const import URL, URL_SHORT, URL_F, HEADERS_LIST

list_card_url = []

total_count = input('Вкажіть кількість сторінок для пасингу : \n')

for count in range(1, int(total_count)+1):
    sleep(3)# pausa == 3 sec
    print('-------------------------------------Парсимо сторінку :', count)
    url = f"{URL_F}+{count}"
    response = requests.get(url, headers=HEADERS_LIST)
    soup = BeautifulSoup(response.text, "lxml") #html.parser
    data = soup.find_all("div",class_="w-full rounded border")

    for i in data:
        card_url = URL_SHORT + i.find("a").get('href')
        list_card_url.append(card_url)

for card_URL in list_card_url:
    response = requests.get(card_URL, headers=HEADERS_LIST)
    soup = BeautifulSoup(response.text, "lxml")  # html.parser
    data_card = soup.find("div", class_="my-8 w-full rounded border")

    name = data_card.find("h3", class_="card-title").text
    price = data_card.find("h4", class_="my-4 card-price").text.replace('$',"")
    description = data_card.find("p", class_="card-description").text
    url_img = URL_SHORT + data_card.find('img', class_="card-img-top").get('src')

    print(f'{name} :\n{price} \n{description}\n{url_img}')



print('Парсинг сторінок завершено')

