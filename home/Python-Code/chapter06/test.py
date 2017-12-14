#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 11:13
# @Author  : deng
# @Site    : 
# @File    : test.py
# @Software: PyCharm

river = {
    "changjiang": "china",
    "nile": "egypt",
    "yellow river": "unkonwn"
}

for name,country in river.items():
    print("the "+name+" runs through "+ country)

#每条河流的名字
for name in river.keys():
    print("river is: "+ name)

#流经的国家
for country in river.values():
    print("country is :" + country)