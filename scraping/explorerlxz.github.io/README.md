# 爬取我的个人博客

## 爬取主页

```python
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
links = "https://explorerlxz.github.io"
html = urlopen(links)
bsObj = BeautifulSoup(html, "lxml")
print(bsObj)
```

输出信息保存到文件中：


```shell
python3 index.py >> index.html
```

## 爬取主页面的所有链接和标题

```python
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
```

把输出信息保存到文件：

```shell
python3 scrabing.py >>links.txt
```

### 保存主页信息到sqlite3数据库


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
import re

baseurl="https://explorerlxz.github.io"

htmlurl = urlopen(baseurl)
bsObj = BeautifulSoup(htmlurl, "lxml")

conn = sqlite3.connect('blogs.db')

db = conn.cursor()
db.execute('''create table blogs (title text, links text)''')

nameList = bsObj.findAll('a', attrs={"class":"post-link"})
for name in nameList:
    blogtitle = name.get_text()
    blogurl = baseurl + name.get('href')
    db.execute('''insert into blogs(title,links)  values(?,?)''', (blogtitle, blogurl))

conn.commit()   #very important
```
