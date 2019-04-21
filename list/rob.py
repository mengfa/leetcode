# -*- coding: utf-8 -*-

#    File Name：       rob
#    Description :
#    Author :          LvYang
#    date：            2019/3/25
#    Change Activity:  2019/3/25:

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int[2,1,1,2]
        """
        d = 0
        s = 0
        for i in range(len(nums)):
            if i%2 == 0:
                print(nums[i])
                s = s+nums[i]
                print(s)
            else:
                print(nums[i])
                d = d + nums[i]
                print(d)
        if s > d:
            return s
        else:
            return d


nums = [2,1,1,2]
so = Solution()
a=so.rob(nums)
print(a)