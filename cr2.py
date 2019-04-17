#this source is to get simple ex01.tml
from bs4 import BeautifulSoup
import requests

#read file from network, zerobizcoin@nate.com
baseurl = 'http://ec2-13-125-20-194.ap-northeast-2.compute.amazonaws.com//quizbot/ex01'
baseurl = 'http://13.125.20.194/quizbot/ex01'

html = requests.get(baseurl).text
soup = BeautifulSoup(html, 'lxml')

#bring text from p tag
exclass_div = soup.find("div", {'class':'ex_class'})
message_p = exclass_div.find_all("p")
print(message_p[1].get_text())
