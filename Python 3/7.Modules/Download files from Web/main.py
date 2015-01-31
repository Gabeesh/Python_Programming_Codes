from urllib import request

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=FB&d=11&e=22&f=2014&g=d&a=4&b=18&c=2012&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_url.split("\\n")
    destination_url = r'fbs.csv'
    file = open(destination_url,"w")
    for line in lines :
        file.write(line + "\n")

    file.close()

download_stock_data(goog_url)
