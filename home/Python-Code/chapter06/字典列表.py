#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 11:39
# @Author  : deng
# @Site    : 
# @File    : 字典列表.py
# @Software: PyCharm

# 嵌套

aliens_0 = {'color': 'green', 'points': 5}
aliens_1 = {'color': 'yellow', 'points': 10}
aliens_2 = {'color': 'red', 'points': 15}

aliens = [aliens_0, aliens_1, aliens_2]

for alien in aliens:
    print(alien)

# 使用range自动生成alien
# 创建列表
aliens_range = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens_range.append(new_alien)

# 显示前五个
for alien in aliens_range[:5]:
    print(alien)
print('------------')

# 显示创建了多少外星人
print(str(len(aliens_range)))
