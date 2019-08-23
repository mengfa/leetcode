# -*- coding: utf-8 -*-

#    File Name：       1.17 从字典中提取子集
#    Description :
#    Author :          LvYang
#    date：            2019/8/22
#    Change Activity:  2019/8/22:

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# # Make a dictionary of all prices over 200
# p1 = {key: value for key, value in prices.items() if value > 200}
#
#
# print(p1)
# # Make a dictionary of tech stocks
# tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# p2 = {key: value for key, value in prices.items() if key in tech_names}
print()

p3 = dict((key, value) for key, value in prices.items() if value > 200)

# print(p3)
p4 = ((key, value) for key, value in prices.items() if value > 200)
for i in p4:
    print(i)


p4 = ((key, value) for key, value in prices.items())
for i in p4:
    print(i)


# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p5 = { key:prices[key] for key in prices.keys() & tech_names }
print(p5)