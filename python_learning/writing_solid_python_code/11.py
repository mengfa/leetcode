# -*- coding: utf-8 -*-

#    File Name：       11
#    Description :
#    Author :          LvYang
#    date：            2020/4/20
#    Change Activity:  2020/4/20:

#枚举替代:
#1. 累属性
from collections import namedtuple


class Seasons:
    Sprint = 0
    Summer = 1
    Autumn = 2
    Winer = 3

print(Seasons.Sprint)

class Seasons2:
    Sprint, SUmmer, Autumn, Winter = range(4)

print(Seasons2.Sprint)

#2. 借助函数
def enum(*posarg, **keysarg):
    return type("Enum", (object,),dict(zip(posarg, range(len(posarg))), **keysarg))

Seasons3 = enum("Spring","Summer","Autumn",Winter=1)
print(Seasons3.Spring)

#3. 使用collections.namedtuple
Seasons4 = namedtuple('Seasons', 'Spring Summer Autumn Winter' )._make(range(4))
print(Seasons4.Summer)