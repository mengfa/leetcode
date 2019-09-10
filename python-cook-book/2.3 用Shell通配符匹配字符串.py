# -*- coding: utf-8 -*-

#    File Name：       2.3 用Shell通配符匹配字符串
#    Description :
#    Author :          LvYang
#    date：            2019/8/26
#    Change Activity:  2019/8/26:

from fnmatch import fnmatch, fnmatchcase
fnmatch('foo.txt', '*.txt')
fnmatch('foo.txt', '?oo.txt')
fnmatch('Dat45.csv', 'Dat[0-9]*')

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

print([name for name in names if fnmatch(name, '*.csv')])

# 区分大小写
fnmatchcase('foo.txt', '*.TXT')

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print([addr for addr in addresses if fnmatch(addr,'*ST')])
