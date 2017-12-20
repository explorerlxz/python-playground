from bs4 import BeautifulSoup as bs
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
    randomIP = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(
        random.randint(0, 255)) + '.' + str(random.randint(0, 255))
    headers = { 
        'User-Agent': random.choice(uas),
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        'X-Forwarded-For': randomIP,
    }   
    return headers

def getContent(url,stream=False):
    try:
        s = requests.Session()
        retries = Retry(total= 5,
                        backoff_factor=10,
                        status_forcelist=[500,502,503,504]
                        )
        s.mount('http://',HTTPAdapter(max_retries= retries))
        return s.get(url,headers = setHeader(),stream=stream)
    except ConnectionResetError:
        print('ConnectionResetError')
        time.sleep(10)
        getContent(url,stream=False)
    except http.client.IncompleteRead:
        print('http.client.IncompleteRead')
        time.sleep(10)
        getContent(url,stream=False)

r = getContent(url)
# print(r.status_code)

soup = bs(r.text, 'lxml')

