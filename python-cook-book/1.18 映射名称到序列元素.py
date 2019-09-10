# -*- coding: utf-8 -*-

#    File Name：       1.18 映射名称到序列元素
#    Description :
#    Author :          LvYang
#    date：            2019/8/23
#    Change Activity:  2019/8/23:

from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)

# Subscriber(addr='jonesy@example.com', joined='2012-10-19')
print(sub.addr)

print(sub.joined)

print(sub)

# Subscriber(addr='jonesy@example.com', joined='2012-10-19')

def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


from collections import namedtuple



Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost1(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


s = Stock('ACME', 100, 123.45)

# s.shares = 75
# 更改不了

s1 = s._replace(shares=75)
print(s1)
print(s)

from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock 创建元祖的方法.
def dict_to_stock(s):
    return stock_prototype._replace(**s)