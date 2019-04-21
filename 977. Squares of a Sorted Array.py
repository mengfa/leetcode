# -*- coding: utf-8 -*-

#    File Name：       977. Squares of a Sorted Array
#    Description :
#    Author :          LvYang
#    date：            2019/4/10
#    Change Activity:  2019/4/10:

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for i in A:
            res.append(i * i)
        res.sort()
        return res

input = [-4,-1,0,3,10]
so = Solution()
print(so.sortedSquares(input))