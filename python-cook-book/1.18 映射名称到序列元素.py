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