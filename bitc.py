from bs4 import BeautifulSoup
import requests

baseurl = 'https://www.bithumb.com/'

html = requests.get(baseurl).text
soup = BeautifulSoup(html, 'lxml')

ntc = soup.find("div", {'class':'global_width ct'})
ntcl = ntc.find_all("dd")

for i in range(len(ntcl)):
    print (ntcl[i].get_text()) 
    url = ntcl[i].find("a")["onclick"]
    pos = url.find("https")

    print(url[pos: len(url)-2])
    
    

 
    
    
    

