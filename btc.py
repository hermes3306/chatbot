
import requests

url = "https://api.bithumb.com/public/ticker/BTC"
response = requests.get(url)

cont = response.json()
print(cont)

print("\n\n\n\n")
print(cont["data"]["closing_price"])

url = "https://api.bithumb.com/public/ticker/ALL"
response = requests.get(url)


cont = response.json()
i = 1
for x in cont['data']:
    if(x=='date'):
        continue;
    print(i, x, cont['data'][x]['closing_price'])
    i+=1
    

