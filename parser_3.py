# import requests
from requests import Session
from bs4 import BeautifulSoup
from time import sleep
from const import URL, URL_SHORT, URL_F, HEADERS_LIST, PATH_DOWNLOADS,URL_SHORT_LOGIN


total_count = input('Вкажіть кількість сторінок для пасингу : \n')

work = Session()
work.get(URL_SHORT_LOGIN)








