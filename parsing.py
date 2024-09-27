import requests
from bs4 import BeautifulSoup
from database.sq_db import create_ncs_table, insert_ncs


create_ncs_table()

for i in range(1, 21):
    url = f'https://colorscheme.ru/ncs-colors-{i}.html'

    q = requests.get(url)
    markup = q.content

    soup = BeautifulSoup(markup, 'lxml')
    colors = soup.find_all('tr')[1:]

    for color in colors:
        td_s = color.find_all('td')

        ncs = td_s[1].text.split()[-1]
        html = td_s[6].text
        r = int(td_s[7].text)
        g = int(td_s[8].text)
        b = int(td_s[9].text)
        c = int(td_s[2].text)
        m = int(td_s[3].text)
        y = int(td_s[4].text)
        k = int(td_s[5].text)

        insert_ncs(ncs, html, r, g, b, c, m, y, k)
