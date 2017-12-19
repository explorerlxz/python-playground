# 获取王垠博客的数据


## 获取目录及链接


```html
        <li class="list-group-item title">
            <a href="/blog-cn/2017/11/04/alphago-zero">AlphaGo Zero 和强人工智能</a>
        </li>
    
        <li class="list-group-item title">
            <a href="/blog-cn/2017/11/01/power-of-reasoning">理性的力量</a>
        </li>

```


```python
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
links = "http://www.yinwang.org"
html = urlopen(links)
bsObj = BeautifulSoup(html, "lxml")

nameList = bsObj.findAll('li', attrs={"class":"list-group-item title"})
for name in nameList:
    print(links + name.find('a', attrs={'href': re.compile("^/blog-cn")}).get('href'))
    print(name.get_text())
```


## 获取所有博客文章，并保存到为html格式


```python
from urllib.request import urlopen
import re, time, os, sys
from bs4 import BeautifulSoup
def getArticle(url):
    time.sleep(0.5)# 防止封IP
    contents = urlopen(url).read()
    soup = BeautifulSoup(contents, "lxml")
    title = soup.find('title').get_text()
    f=open('./articles/' + title+'.html', 'wb')
    f.write(contents)
    f.close


links = "http://www.yinwang.org"
html = urlopen(links)
bsObj = BeautifulSoup(html, "lxml")

nameList = bsObj.findAll('li', attrs={"class":"list-group-item title"})
linkList = []
for name in nameList:
    #把所有文章的链接保存到linkList中
    linkList.extend([links + name.find('a', attrs={'href': re.compile("^/blog-cn")}).get('href')])

for articleUrl in linkList:
    getArticle(articleUrl)

```
