# 获取文学网站目录及文章


这个网页好像挺复杂的，用gbk也不能完全正确解码。

```python
from bs4 import BeautifulSoup as bs
import urllib.request
import sqlite3
import random


url = 'http://blog.boxun.com/hero/majian/'

# 设置 user-agent列表，每次请求时，可在此列表中随机挑选一个user-agnet
uas = [ 
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.96 Chrome/58.0.3029.96 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
    "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
    ]   

def setHeader():
    headers = {'User-Agent': random.choice(uas)}
    return headers

url = 'http://blog.boxun.com/hero/majian/'

head = setHeader()

request = urllib.request.Request(url, None, head)
response = urllib.request.urlopen(request)
#bsObj = bs(response, 'lxml')
html = response.read()
#html = html.encode('gbk').decode('utf8')
html = html.decode('gbk')#按照gbk解码
print(html)
```
