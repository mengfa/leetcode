# -*- coding: utf-8 -*-

#    File Name：       2.1 使用多个界定符分割字符串
#    Description :
#    Author :          LvYang
#    date：            2019/8/23
#    Change Activity:  2019/8/23:

line = 'asdf fjdk; afed, fjek,asdf, foo'

import re

r = re.split(r'[;,\s]\s*', line)

print(r)