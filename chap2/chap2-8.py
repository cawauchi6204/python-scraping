import requests
from bs4 import BeautifulSoup

load_url = 'https://news.yahoo.co.jp/categories/it'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

filename = 'linklist.txt'
topic = soup.find(id='uamods-topics')
with open(filename, 'w') as f:
    for element in topic.find_all('a'):
        url = element.get('href')
        f.write(element.text + '\n')
        url = element.get('href')
        f.write(url + '\n')
        f.write('\n')
