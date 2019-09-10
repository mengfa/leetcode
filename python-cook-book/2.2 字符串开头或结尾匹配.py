# -*- coding: utf-8 -*-

#    File Name：       2.2 字符串开头或结尾匹配
#    Description :
#    Author :          LvYang
#    date：            2019/8/26
#    Change Activity:  2019/8/26:

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))


filenames = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
print([name for name in filenames if name.endswith(('.c', '.h'))])

print(any(name.endswith('.py') for name in filenames))