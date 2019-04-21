# -*- coding: utf-8 -*-

#    File Name：       TwoSum
#    Description :
#    Author :          LvYang
#    date：            2019/4/1
#    Change Activity:  2019/4/1:

# 执行用时为 20 ms 的范例
class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, nums, target):
        d={}
        for i,num in enumerate(nums):
            print('-----')
            print(target, num, d)
            if target-num in d:
                return [d[target-num], i]
            print(i, num, d)
            d[num] = i


nums = [2, 7, 11, 15]
target = 18
so = Solution()
res = so.twoSum(nums, target)
print(res)