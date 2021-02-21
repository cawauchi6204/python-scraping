import requests
from bs4 import BeautifulSoup

load_url = 'https://www.ymori.com/books/python2nen/test2.html'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

filename = 'linklist.txt'
with open(filename, 'w') as f:
    for element in soup.find_all('a'):
        f.write(element.text + '\n')
        url = element.get('href')
        f.write(url + '\n')
        f.write('\n')
