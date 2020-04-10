# -*- coding: utf-8 -*-

#    File Name：       8-assert
#    Description :
#    Author :          LvYang
#    date：            2020/4/9
#    Change Activity:  2020/4/9:

x = 1
y = 2
assert x == y, "not equals"


if __debug__ and not x == y:
    raise AssertionError("not equals")

assert isinstance(input, list), 'input must be type of list'