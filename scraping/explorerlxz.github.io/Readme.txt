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


```
python3 index.py >> index.html
```

## 爬取主页面的所有链接和标题。

```
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

```
python3 scrabing.py >>links.txt
```


