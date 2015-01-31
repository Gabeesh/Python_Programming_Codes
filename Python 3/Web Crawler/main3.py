import requests
from bs4 import BeautifulSoup

url2='https://www.google.co.in/webhp?source=search_app&gws_rd=cr&ei=NiYvUpfyCImJrgeuq4HoCQ#q=cars+in+india&start=30'
url1 = 'https://www.thenewboston.com/trade/search.php?page=1'

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.thenewboston.com/trade/search.php?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = 'https://www.thenewboston.com' + link.get('href')
            title = link.string
            #print(href)
            #print(title)
            get_single_item_data(href)

        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div', {'class': 'i-name'}):
        print (item_name.string)




trade_spider(3)
