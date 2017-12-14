#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 14:00
# @Author  : deng
# @Site    : 
# @File    : pizzy.py
# @Software: PyCharm


pizzy = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

#描述所点的披萨
print('you ordered a '+ pizzy['crust']+'-crust pizza'
      + 'with the following toppings:')

for topping in pizzy['toppings']:
    print(topping)