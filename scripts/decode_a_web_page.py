import requests
from bs4 import BeautifulSoup

url = 'http://www.wafb.com'
r = requests.get(url)
r_html = r.text

print(r.text)

soup = BeautifulSoup(r_html, features="html.parser")
title = soup.find('span', 'title').string
