# -*- coding: utf-8 -*-

#    File Name：       singlenumber
#    Description :
#    Author :          LvYang
#    date：            2019/9/10
#    Change Activity:  2019/9/10:


# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         temp = {}
#         for i in nums:
#             if i in temp.keys():
#                 temp.pop(i)
#                 print(temp)
#             else:
#                 temp[i]=0
#                 print(temp)
#         return list(temp.keys())[0]
from functools import reduce


class Solution(object):
    def singleNumber(self, nums):
        return reduce(int.__xor__, nums)

input = [4, 1, 2, 1, 2]

so = Solution()
output = so.singleNumber(input)
print(output)
