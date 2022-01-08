import requests
from bs4 import BeautifulSoup

url=requests.get("https://www.haberler.com/")
##print(url.text)

soup= BeautifulSoup(url.content,"html.parser")
##for i in soup.find_all("p"):
  ##  print(i.text)
for i in soup.find_all("p",attrs={"class":"hbBoxText"}):
    print(i.string)