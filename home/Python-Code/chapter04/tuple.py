#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1 10:59
# @Author  : deng
# @Site    : 
# @File    : tuple.py
# @Software: PyCharm

#列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网
#站的用户列表或游戏中的角色列表至关重要。然而，有时候你需要创建一系列不可修改的元素，
#元组可以满足这种需求。Python将不能修改的值称为不可变的，而不可变的列表被称为元组

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0]=5  # 这一行会报错，元组的元素不能修改

# 虽然不能修改元组的元素，但是可以给存储元组的变量赋值
dimensions = (100,20)
print(dimensions)

# <h1>如果需要存储的一组值在程序的整个生命周期内都不可变，可使用元组</h1>