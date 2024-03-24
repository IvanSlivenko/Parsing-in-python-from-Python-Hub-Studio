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
    # print(list_card_url)


for card_url in list_card_url:
    response = requests.get(card_url, headers=HEADERS_LIST)
    soup = BeautifulSoup(response.text, "lxml")  # html.parser
    data_card = soup.find("div", class_="my-8 w-full rounded border")
    name = data_card.find('h3').text
    print(name)


        # name = i.find('h4').text.replace("\n","")
        # price = i.find('h5').text.replace("$","")
        # url_img = URL_SHORT + i.find("img", class_="card-img-top img-fluid").get("src")
        # print(name+"\n"+price+"\n"+url_img+"\n\n")

print('Парсинг сторінок завершено')

