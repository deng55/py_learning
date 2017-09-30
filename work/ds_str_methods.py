#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/31 12:53
# @Author  : deng
# @Site    : 
# @File    : ds_str_methods.py
# @Software: PyCharm

name = 'Swaroop'

if name.startswith('Swa'):
    print('yes, the string start with Swa')

if 'a' in name:
    print('yes , the string contains "a"')

if name.find('war') != -1:
    print('yes, the string contains "war"')

delimiter = '_*_'
myList = ['a', 'b', 'c', 'd']
print(delimiter.join(myList))
