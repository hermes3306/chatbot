from bs4 import BeautifulSoup
import requests

baseurl = 'https://www.bithumb.com/trade/order/BTC'

html = requests.get(baseurl).text
soup = BeautifulSoup(html, 'lxml')

d1 = soup.find("table", {'class':'table_st1', 'id':'tableAsset'  })

print(d1) 
    
    
    
