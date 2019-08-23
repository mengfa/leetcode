# -*- coding: utf-8 -*-

#    File Name：       1.8
#    Description :
#    Author :          LvYang
#    date：            2019/8/19
#    Change Activity:  2019/8/19:

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

a = zip(prices.values(),prices.keys())

b = list(a)
print(b)

for i in a:
    print(i)

min_price = min(zip(prices.values(),prices.keys()))
print(min_price)