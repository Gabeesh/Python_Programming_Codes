import requests
from bs4 import BeautifulSoup

url2='https://www.google.co.in/webhp?source=search_app&gws_rd=cr&ei=NiYvUpfyCImJrgeuq4HoCQ#q=cars+in+india&start=30'

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        #url2='https://www.google.co.in/webhp?source=search_app&gws_rd=cr&ei=NiYvUpfyCImJrgeuq4HoCQ#q=cars+in+india&start='+str(page)
        url = 'https://www.thenewboston.com/trade/search.php?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = link.get('href')
            print(href)
            page += 1

trade_spider(1)

