from bs4 import BeautifulSoup
import requests

baseurl = 'http://13.125.20.194/quizbot/ex01'

html = requests.get(baseurl).text
soup = BeautifulSoup(html, 'lxml')

h2 = soup.find("h2")
a = h2.find("a")


print(a['href'])



  
    
    

