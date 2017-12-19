from urllib.request import urlopen
import re, time, os, sys
from bs4 import BeautifulSoup
def getArticle(url):
#    time.sleep(0.5)# 防止封IP
    contents = urlopen(url).read()
    soup = BeautifulSoup(contents, "lxml")
    title = soup.find('title').get_text()
#    print(title.get_text())
    f=open('./articles/' + title+'.html', 'wb')
    f.write(contents)
    f.close
#    return urlopen(url).read()


links = "http://www.yinwang.org"
html = urlopen(links)
bsObj = BeautifulSoup(html, "lxml")

nameList = bsObj.findAll('li', attrs={"class":"list-group-item title"})
linkList = []
for name in nameList:
    linkList.extend([links + name.find('a', attrs={'href': re.compile("^/blog-cn")}).get('href')])

for articleUrl in linkList:
    getArticle(articleUrl)

#print(linkList)
#    print(name.get_text())



