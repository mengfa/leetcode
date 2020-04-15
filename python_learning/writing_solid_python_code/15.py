# -*- coding: utf-8 -*-

#    File Name：       15
#    Description :
#    Author :          LvYang
#    date：            2020/4/15
#    Change Activity:  2020/4/15:

def myenumerate(sequence):
    n = -1
    for elem in reversed(sequence):
        yield len(sequence)+n, elem
        n = n-1

li = ['a', 'b', 'c', 'd', 'e']
for i, e in myenumerate(li):
    print("inde: {}, element: {}".format(i, e))
