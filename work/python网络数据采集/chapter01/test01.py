#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/30 17:44
# @Author  : deng
# @Site    : 
# @File    : test01.py
# @Software: PyCharm

from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
else:
    bsObj = BeautifulSoup(html.read())
    print(bsObj.h1)

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    bsObj = BeautifulSoup(html.read())
    badObj = bsObj.nonExistenTag.anotherTag
except AttributeError as e:
    print(e)
else:
    if badObj == None:
        print('tag was not found')
    else:
        print(badObj)

