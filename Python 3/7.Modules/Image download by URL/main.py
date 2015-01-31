import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    real_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url,real_name)

download_web_image('https://www.thenewboston.com/photos/users/622/resized/caee9a05b14920f5c5e30e0f0f023d39.jpg')