# -*- coding: utf-8 -*-

#    File Name：       1.7字典排序
#    Description :
#    Author :          LvYang
#    date：            2019/8/19
#    Change Activity:  2019/8/19:

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])