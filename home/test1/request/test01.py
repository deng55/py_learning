import requests

r = requests.get("https://www.taobao.com")

print(r.headers)