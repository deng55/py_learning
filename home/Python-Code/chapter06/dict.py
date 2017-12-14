#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/7 11:44
# @Author  : deng
# @Site    : 
# @File    : dict.py
# @Software: PyCharm


# 遍历所有键值对

user_0 = {
    'username': 'tom',
    'first': 'enric',
    'last': 'fermi'
}

for key, value in user_0.items():
    print('\nkey: ' + key.title())
    print('value: ' + value)

print('*************')
# 遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


for name in favorite_languages.keys(): # 加不加keys结果不变 默认遍历所有的键
    print('name: '+name)

print('*********')
# ********
# 按顺序遍历所有的键
for name in sorted(favorite_languages):
    print("name: "+name+" thank you")

# 遍历字典中的所有值
for language in favorite_languages.values():
    print("language is : "+language)

    #使用set来提取favorite_language中的语言，去重
for language in set(favorite_languages.values()):
    print(language)

print('*******')
persons = ['jack','jen','tom','sarah']
for person in persons:
    if person in favorite_languages.keys():
        print('thanks for your work '+ person)
    else:
        print('I\'d like to invite you to join the interview '+ person)