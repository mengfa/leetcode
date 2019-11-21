# -*- coding: utf-8 -*-

#    File Name：       131. Palindrome Partitioning
#    Description :
#    Author :          LvYang
#    date：            2019/9/18
#    Change Activity:  2019/9/18:
'''
分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

# class Solution(object):
#     def partition(self, s):
#         """
#         :type s: str
#         :rtype: List[List[str]]
#         """
#
#         res = []
#         def dfs(s, path):
#             if not s:
#                 res.append(path)
#                 return
#             for i in range(1,len(s)+1):
#                 if s[:i] == s[:i][::-1]:
#                     dfs(s[i:], path+[s[:i]])
#         dfs(s, [])
#         return res


# 执行用时为32ms的范例


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []

        res = [[]]
        for i, x in enumerate(s):
            tmp = []
            print("1--i: {}, x: {}, res: {}, tmp: {}".format(i, x, res, tmp))
            for r in res:
                print("1.1r: {}  x: {}, tmp: {}".format(r, x, tmp))
                tmp.append(r + [x])
                # print("2--r[-1]: {}, x: {}".format(r[-1], x))
                if len(r) >= 1 and r[-1] == x:
                    print("2.1--r: {}, r[-1]: {}, x: {}, tmp: {}".format(r, r[-1], x, tmp))
                    tmp.append(r[:-1] + [r[-1] + x])
                    print("2.1--tmp: {}".format(tmp))
                if len(r) >= 2 and r[-2] == x:
                    print("2.2--r: {}, r[-2]: {}, x: {}, tmp: {}".format(r, r[-2], x, tmp))
                    tmp.append(r[:-2] + [r[-2] + r[-1] + x])
                    print("2.1--tmp: {}".format(tmp))

                print("--------n")
            res = tmp
            print("3---i: {}, x: {}, res: {}, ".format(i, x, res))
            print("--------------------")

        return res
input = "aaba"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

so = Solution()
print(so.partition(input))
