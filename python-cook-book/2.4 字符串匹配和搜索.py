# -*- coding: utf-8 -*-

#    File Name：       2.4 字符串匹配和搜索
#    Description :
#    Author :          LvYang
#    date：            2019/9/4
#    Change Activity:  2019/9/4:

# 2.4 字符串匹配和搜索

text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print(text == 'yeah')
# Match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))
# Search for the location of the first occurrence
print(text.find('no'))


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')


if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))


print("--------------------------------------")
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')

print(m)