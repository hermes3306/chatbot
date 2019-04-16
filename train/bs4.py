import requests

url="http://118.221.137.114:9000/tot/getjson"

resp=requests.get(url)
content=resp.json()
print(content)

