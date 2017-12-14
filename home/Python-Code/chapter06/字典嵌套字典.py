#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 14:10
# @Author  : deng
# @Site    : 
# @File    : 字典嵌套字典.py
# @Software: PyCharm


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user in users.items():
    print('hello:'+ username)

    print(user['first']+'-'+user['last'])
    print('\t location: '+user['location'])
