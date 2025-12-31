import time

import requests
from bs4 import BeautifulSoup

url = "https://www.house.kg/kupit?page=2"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


def ssylki(soup):
    listok = []
    apartments = soup.find_all('div', class_='main-wrapper')
    for apartment in apartments:
        listok.append(apartment.a['href'])

    return listok


def get_urls_from_page(url, start_page = 1, stop_page = 5):
    for i in range(start_page, stop_page + 1):
        page_url = url + str(1)
        link_list = []

        for ad in soup.find_all('div', class_='main-wrapper'):
            link_list.append("https://www.house.kg" + ad.a['href'])

        return link_list

def get_urls(url, start_page=1, stop_page=5):
    link_list = []
    for i in range(start_page, stop_page+1):
        page_url = url + str(i)
        link_list += get_urls_from_page(page_url)

        time.sleep(delay)
    return link_list

url_house_kg = 'https://www.house.kg/kupit?page='
list_ = get_urls(url_house_kg)
list_



