# -*- coding: utf-8 -*-

#    File Name：       1.13 通过某个关键字排序一个字典列表
#    Description :
#    Author :          LvYang
#    date：            2019/8/22
#    Change Activity:  2019/8/22:

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)
# 这个r就是rows的迭代的子元素.
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
print(rows_by_lfname)