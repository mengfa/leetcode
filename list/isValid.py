# -*- coding: utf-8 -*-

#    File Name：       isValid
#    Description :
#    Author :          LvYang
#    date：            2019/3/26
#    Change Activity:  2019/3/26:
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        paren_map = {')': '(', ']': '[', '}': '{'}
        for c in s:

            if c not in paren_map:
                print("if c: {}".format(c))
                stack.append(c)
            elif not stack or paren_map[c] != stack.pop():
                return False
        return not stack

input = "()[]{}"

so = Solution()
result = so.isValid(input)
print(result)