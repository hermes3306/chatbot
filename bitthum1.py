from bs4 import BeautifulSoup
import requests

baseurl = 'https://www.bithumb.com/'

html = requests.get(baseurl).text
soup = BeautifulSoup(html, 'lxml')



ntc = soup.find("div", {'class':'global_width ct'})
'''
print (ntc)
'''


'''
soup.find("meta", {"name":"City"})['content']
'''

ntcl = ntc.find_all("dd")
print ("<a>:" , ntcl[0].find("a"))
print ("<a>:" , ntcl[0].find("a"))

print ("get_text(): ", ntcl[0].get_text())
print ("get_text(): ", ntcl[1].get_text())
print ("get_text(): ", ntcl[2].get_text())
print ("get_text(): ", ntcl[3].get_text())




