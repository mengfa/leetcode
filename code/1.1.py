# -*- coding: utf-8 -*-

#    File Name：       1.1
#    Description :
#    Author :          LvYang
#    date：            2019/8/15
#    Change Activity:  2019/8/15:

# print('1')
# records = [
#     ('foo', 1, 2),
#     ('bar', 'hello'),
#     ('foo', 3, 4),
# ]
#
# def do_foo(x,y):
#     print('foo', x, y)
# def do_bar(s):
#     print('bar', s)
#
# for s, *args in records:
#     if s == 'bar':
#         do_bar(*args)
#     if s == 'foo':
#         do_foo(*args)


items = [1, 10, 7, 4, 5, 9]
def sum(items):
    print(items)
    head, *tail = items
    print(head, tail)
    return head + sum(tail) if tail else head

# print(sum(items))

a = []
b = [1, 2, 3]

print(sum(a) if a else b)