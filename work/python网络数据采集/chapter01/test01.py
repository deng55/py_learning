#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/30 17:44
# @Author  : deng
# @Site    : 
# @File    : test01.py
# @Software: PyCharm

from urllib.request import urlopen

html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())