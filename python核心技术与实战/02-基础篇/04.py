# -*- coding: utf-8 -*-

#    File Name：       04
#    Description :
#    Author :          LvYang
#    date：            2019/11/22
#    Change Activity:  2019/11/22:

# import time
#
#
# def find_unique_price_using_set(products):
#     unique_price_set = set()
#     for _, price in products:
#         unique_price_set.add(price)
#     return len(unique_price_set)
#
#
# def find_unique_price_using_list(products):
#     unique_price_list = []
#     for _, price in products:  # A
#         if price not in unique_price_list:  # B
#             unique_price_list.append(price)
#     return len(unique_price_list)
#
#
# id = [x for x in range(0, 100000)]
# price = [x for x in range(200000, 300000)]
# products = list(zip(id, price))
#
# # 计算列表版本的时间
# start_using_list = time.perf_counter()
# find_unique_price_using_list(products)
# end_using_list = time.perf_counter()
# print("time elapse using list: {}".format(end_using_list - start_using_list))
# ## 输出
# # time elapse using list: 41.61519479751587
#
# # 计算集合版本的时间
# start_using_set = time.perf_counter()
# find_unique_price_using_set(products)
# end_using_set = time.perf_counter()
# print("time elapse using set: {}".format(end_using_set - start_using_set))
# # 输出
# # time elapse using set: 0.008238077163696289

d = {'name': 'jason', ['education']: ['Tsinghua University', 'Stanford University']}
print(d)