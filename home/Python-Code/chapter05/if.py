#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1 11:48
# @Author  : deng
# @Site    : 
# @File    : if.py
# @Software: PyCharm

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


age_0 = 22
age_1 = 23
print(age_0>age_1 and age_0 >= 21)
print(age_0>age_1 or age_0 >= 21)

# 检查特定值是否包含在列表中 使用关键字 in

# 检查特定值是否不包含在列表中 使用 not in
if age_0<4:
    print('a')
elif age_0<17:
    print('b')
else:
    print('c')


fruits = ['apple', 'pear', 'banana']
if 'apple' in fruits and 'pear' in fruits:
    print('success')