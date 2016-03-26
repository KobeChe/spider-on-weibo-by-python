# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time



cook = {"Cookie":"YOUR_COOkie"}

for i in range(1,20):

    url = "http://weibo.cn/breakingnews?page=%d"%(i)

    html = requests.get(url,cookies=cook).content

    #print(html.decode('utf-8'))

    soup =BeautifulSoup(html,"html.parser")

    r = soup.findAll('span',attrs={"class" : "ctt"})
    for e in r:
        print(e.text)

    time.sleep(3)

