from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
links = "https://explorerlxz.github.io"
html = urlopen(links)
bsObj = BeautifulSoup(html, "lxml")

nameList = bsObj.findAll('a', attrs={"class":"post-link"})
for name in nameList:
    print(links + name.get('href'))
    print(name.get_text())

