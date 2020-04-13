# -*- coding: utf-8 -*-

#    File Name：       9-swap
#    Description :
#    Author :          LvYang
#    date：            2020/4/9
#    Change Activity:  2020/4/9:

from timeit import Timer

print(Timer('temp = x;x = y;y = temp', 'x=2;y=3').timeit())

print(Timer('x, y = y, x', 'x=2;y=3').timeit())

import dis

def swap1():
    x = 2
    y = 3
    x, y = y, x

def swap2():
    x = 2
    y = 3
    temp = x
    x = y
    y = temp

print("swap1():")
dis.dis(swap1)
print("swap2():")
dis.dis(swap2)
