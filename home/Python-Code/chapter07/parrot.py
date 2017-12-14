#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 15:43
# @Author  : deng
# @Site    : 
# @File    : parrot.py
# @Software: PyCharm



message = input('tell me something, and I\'ll repeat it back to you:')
print(message)

height = input("please input you height")
height = int(height)

if height>= 36:
    print('you are tall enough to ride')
else:
    print('you can ride when you are a little older')

