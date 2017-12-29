#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18 12:58
# @Author  : deng
# @Site    : 
# @File    : whileTest.py
# @Software: PyCharm

unconfirmed_user = ['lily', 'tom', 'jack']
confirmed_user = []

while unconfirmed_user:
    current_user = unconfirmed_user.pop()

    print("Verifying user: " + current_user)
    confirmed_user.append(current_user)

# 显示所有已验证的用户
for user in confirmed_user:
    print(user.title())

# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)