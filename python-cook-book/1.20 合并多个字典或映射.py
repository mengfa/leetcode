# -*- coding: utf-8 -*-

#    File Name：       1.20 合并多个字典或映射
#    Description :
#    Author :          LvYang
#    date：            2019/8/23
#    Change Activity:  2019/8/23:

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
# 现在假设你必须在两个字典中执行查找操作（比如先从 a 中找，如果找不到再在 b 中找）。 一个非常简单的解决方案就是使用 collections 模块中的 ChainMap 类。比如：
from collections import ChainMap
c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)


values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3

print(values)

# values
#
# values['x']
# # Discard last mapping
# values = values.parents
# values['x']
# # Discard last mapping
# values = values.parents
# values['x']
# values
