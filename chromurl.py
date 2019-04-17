from bs4 import BeautifulSoup
from selenuium import webdriver
import time

import requests

baseurl = 'https://cafe.bithumb.com/view/board-contents/1640053'

driver=webdriver.Chrome(baseurl)
html = requests.get(baseurl).text

time.sleep(1)
html = driver.page_source

soup = BeautifulSoup(html, 'lxml')


l = soup.find_all("div", {'class':'board-content col-12'}) 
print(l)

for i in l:
    print (p)
