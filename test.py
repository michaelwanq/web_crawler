import requests
from bs4 import BeautifulSoup
import selenium

# url = "http://www.crazyant.net"
url = "http://www.baidu.com"

r = requests.get(url)
r.encoding = "utf-8"
# print(str(r.status_code)+"\n")
# print(r.headers)
# print("\n" + r.encoding+"\n")
print(r.text+"\n")
# print(r.url+"\n")
# print(r.content)
# print("\n" + str(r.cookies))
