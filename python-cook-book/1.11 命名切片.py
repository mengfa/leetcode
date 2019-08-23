# -*- coding: utf-8 -*-

#    File Name：       1.11 命名切片
#    Description :
#    Author :          LvYang
#    date：            2019/8/20
#    Change Activity:  2019/8/20:

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

print(cost)

example = '1234567890'

print(example[:2])

print(example[-2:])

print(example[-2:])

print(example[::-2])


print(example[2:])


c = "          1122     "
print(c.strip())