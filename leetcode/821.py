# -*- coding: utf-8 -*-

#    File Name：       821
#    Description :
#    Author :          LvYang
#    date：            2019/4/12
#    Change Activity:  2019/4/12:

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        li = []
        pos1 = S.find(C)
        # 处理字符串S查找到字符C之前的部分
        for i in range(pos1):
            li.append(pos1 - i)
        pos2 = 0
        # 处理S中间每两个C之间的部分，注意这里pos2不能为-1，否则会出现错误
        while pos2 < S.rfind(C) and pos2 != -1:
            pos2 = S.find(C, pos1 + 1, len(S))# 这里pos2可能返回-1，要在循环条件里排除
            print("pos1 = ", pos1, "pos2 = ", pos2)
            for i in range(pos1, pos2):
                if (i - pos1) <= pos2 - i:
                    li.append(i - pos1)
                else:
                    li.append(pos2 - i)
            pos1 = pos2
        # 处理最后一个字符C到字符串S最后的部分。
        if S.rfind(C) <= len(S) - 1:
            for i in range(S.rfind(C), len(S)):
                li.append(i - S.rfind(C))
        return li

    """
    Input: S = "loveleetcode", C = 'e'
    Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
            [3, 2, 1, 0, 1, 0, 0, 4, 3, 2, 1, 0]      
    """



S = "llllellllll"
C = 'e'
so = Solution()
print(so.shortestToChar(S,C))