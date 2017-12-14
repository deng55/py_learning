#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 14:26
# @Author  : deng
# @Site    : 
# @File    : test2.py
# @Software: PyCharm

dog = {
    'type': 'dog',
    'master': 'tom',
}

cat = {
    'type': 'cat',
    'master': 'jack',
}

monkey = {
    'type': 'monkey',
    'master': 'paul',
}

pets = [dog, cat, monkey]
for pet in pets:
    print('pet\'s name is :' + pet['type'])
    print('pet\'s master is:' + pet['master'])

print('****************************************')

# love places
favorite_places = {
    'tom':['wuhan','suzhou','shenzhen'],
    'jack': ['beijing', 'nanjing', 'shanghai'],
}

for user, places in favorite_places.items():
    print(user+' favoriate places are:')
    for place in places:
        print(place)


print('***********************************')
# city
cities = {
    'wuhan': {
        'country': 'china',
        'population': '15billion'
    },
    'ny': {
        'country': 'us',
        'population': '0.3billion',
    },
    'london': {
        'country': 'uk',
        'population': '70million',
    }
}

for city, detail in cities.items():
    print(city+'\'s details:')
    print("country:"+detail['country'])
    print("population:"+detail['population'])