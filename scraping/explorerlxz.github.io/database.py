from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import sqlite3
baseurl="https://explorerlxz.github.io"

htmlurl = urlopen(baseurl)
bsObj = BeautifulSoup(htmlurl, "lxml")

conn = sqlite3.connect('blogs.db')

db = conn.cursor()
db.execute('''create table blogs (title text, links text)''')

nameList = bsObj.findAll('a', attrs={"class":"post-link"})
for name in nameList:
    blogtitle = name.get_text()
#    print(blogtitle)
    blogurl = baseurl + name.get('href')
#    print(blogurl)
    db.execute('''insert into blogs(title,links)  values(?,?)''', (blogtitle, blogurl))

conn.commit()
