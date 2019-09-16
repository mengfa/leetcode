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
# from functools import reduce
#
# # 这里用到了异或（xor），相同的数字异或后为0，0异或任何数都等于那个数，用reduce在列表所有元素之间使用异或^，那么留下的就是那个单独的数字了。
# class Solution(object):
#     def singleNumber(self, nums):
#         return reduce(int.__xor__, nums)
#
# input = [4, 1, 2, 1, 2]
#
# so = Solution()
# output = so.singleNumber(input)
# print(output)
#
#
# print(4^1)
#
# print(int.__xor__())
# input = [4, 1, 2, 1, 2]
#
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         res = 0
#         for i in nums:
#             print(i, res)
#             res ^= i
#             print(res)
#         return res
#
# so = Solution()
# output = so.singleNumber(input)
# print(output)


input = [4, 1, 2, 1, 2]
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums))*2-sum(nums)



print(set(input))
so = Solution()
output = so.singleNumber(input)
print(output)


class Solution(object):
    def singleNumber(self, nums):
        # kv = []
        # for item in nums:
        #     if item in kv:
        #         kv.remove(item)
        #     else:
        #         kv.append(item)
        # return kv[0]
        count = {}                # 定义字典
        for num in nums:          # 遍历数组
            if num in count:      # 如果字典中存在当前记录
                count[num] += 1   # 次数 + 1
            else:                 # 否则
                count[num] = 1    # 当前数加入到字典中，且出现次数为1
        count = {v: k for k, v in count.items()}  # 字典键值交换
        return count[1]           # 返回出现一次的数字

        """
        :type nums: List[int]
        :rtype: int
        """