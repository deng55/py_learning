#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 16:03
# @Author  : deng
# @Site    : 
# @File    : jsonTest.py
# @Software: PyCharm

import json
from urllib.request import urlopen


def getCountry(ipAddress):
    response = urlopen('http://freegeoip.net/json/' + ipAddress).read().decode(
        'utf-8')
    responseJson = json.loads(response)

    return responseJson.get('country_code')


print(getCountry('58.250.16.228'))
