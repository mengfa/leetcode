# -*- coding: utf-8 -*-

#    File Name：       1.10 删除序列相同元素并保持顺序
#    Description :
#    Author :          LvYang
#    date：            2019/8/20
#    Change Activity:  2019/8/20:

# def dedupe(items):
#     print("items: {}".format(items))
#     seen = set()
#     for item in items:
#         print("item0: {}".format(item))
#         if item not in seen:
#             print("item1: {}".format(item))
#             yield item
#             print("item2: {}".format(item))
#             seen.add(item)
#             print("item3: {}".format(item))
#
# a = [1, 5, 2, 1, 9, 1, 5, 10]


# print(dedupe(a))
# result = list(dedupe(a))
# print(result)

# f = dedupe(a)
# f.__next__()
# print("------------")
# f.__next__()

#--------00


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        print("val: {}".format(val))
        if val not in seen:
            yield item
            seen.add(val)


a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))


print(list(dedupe(a, key=lambda d: d['x'])))

# 如果你仅仅就是想消除重复元素，通常可以简单的构造一个集合。比如：
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))
