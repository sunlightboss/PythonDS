import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1/saison_id/2025'

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

club_list = []


def get_clubs(soup):
    table = soup.find('table', class_='items')
    for row in table.find_all('tr', class_=['odd', 'even']):
        name_td = row.find('td', class_='hauptlink')
        name = name_td.get_text(strip=True) if name_td else ''

        value_td = row.find_all('td', class_='rechts')[-1]
        value = value_td.get_text(strip=True) if value_td else ''

        club_list.append({'name': name, 'value': value})
    return club_list


clubs = get_clubs(soup)
for club in clubs:
    print(f"{club['name']}: {club['value']}")