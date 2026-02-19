import requests
from bs4 import BeautifulSoup

response = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')
book_list = []

def ret_books(soup):
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        dict_ = {}

        link = book.h3.a['href']
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.replace('£', '')

        dict_['name'] = title
        dict_['price'] = price
        dict_['url'] = link
        book_list.append(dict_)
    return book_list


print(ret_books(soup))




