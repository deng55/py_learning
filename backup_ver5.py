#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 12:38
# @Author  : deng
# @Site    : 
# @File    : backup_ver5.py
# @Software: PyCharm

import zipfile
import os

import time

source = ['D:\\test01']

target_dir = 'D:\\backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('enter something-->')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
                 comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('successful created dictionary',today)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print("zip command is")
print(zip_command)

print('running')
if zipfile.ZipFile(zip_command,'w'):
    print('successful',target)
else:

    print('fail')

