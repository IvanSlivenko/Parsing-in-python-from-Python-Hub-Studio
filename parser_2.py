import requests
from bs4 import BeautifulSoup
from time import sleep
from const import URL, URL_SHORT, URL_F, HEADERS_LIST, PATH_DOWNLOADS


total_count = input('Вкажіть кількість сторінок для пасингу : \n')

def download(url):
    resp = requests.get(url, stream=True)
    r = open("D:\\GitHub\\Parsing-in-python-from-Python-Hub-Studio\\image\\" + url.split("/")[-1], "wb")
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_url():
    for count in range(1, int(total_count)+1):

        print('-------------------------------------Парсимо сторінку :', count)
        url = f"{URL_F}+{count}"
        response = requests.get(url, headers=HEADERS_LIST)
        soup = BeautifulSoup(response.text, "lxml") #html.parser
        data = soup.find_all("div",class_="w-full rounded border")

        for i in data:
            card_url = URL_SHORT + i.find("a").get('href')
            yield card_url

def array():
    for card_URL in get_url():

        response = requests.get(card_URL, headers=HEADERS_LIST)
        sleep(3)  # pausa == 3 sec
        soup = BeautifulSoup(response.text, "lxml")  # html.parser
        data_card = soup.find("div", class_="my-8 w-full rounded border")

        name = data_card.find("h3", class_="card-title").text
        price = data_card.find("h4", class_="my-4 card-price").text.replace('$',"").replace(".",",")
        description = data_card.find("p", class_="card-description").text
        url_img = URL_SHORT + data_card.find('img', class_="card-img-top").get('src')

        download(url_img)

        yield name, price, description, url_img

        # print(f'{name} :\n{price} \n{description}\n{url_img}')



