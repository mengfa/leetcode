# -*- coding: utf-8 -*-

#    File Name：       旋转图像
#    Description :
#    Author :          LvYang
#    date：            2019/3/19
#    Change Activity:  2019/3/19:

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        length = len(matrix)
        for i in range(length):
                for j in range(i+1,length):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
                print(matrix)
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
#24ms
class Solution24:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def rotate(self, matrix):
        # write your code here
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()


#执行用时为28ms的范例
'''
1.需要对一层一层的正方形进行旋转
2.在每一层中，分别有四个数字时对应的可以进行置换
#(tv,th)--------------   (top vertical,top horizen) (last vertical,last horizen)
#|                    |
#|                    |
#|                    |
#|                    |
#|                    |
#|                    |
#-----------------(lv,lh)
'''
class Solution28(object):
    def rotateedge(self, matrix, tv, th, lv, lh):
        for i in range(lv - tv):
            temp = matrix[tv][th + i]
            matrix[tv][th + i] = matrix[lv - i][th]
            matrix[lv - i][th] = matrix[lv][lh - i]
            matrix[lv][lh - i] = matrix[tv + i][lh]
            matrix[tv + i][lh] = temp

    def rotate(self, matrix):
        tv, th, lv, lh = 0, 0, len(matrix) - 1, len(matrix) - 1
        while tv < lv:
            self.rotateedge(matrix, tv, th, lv, lh)
            tv += 1
            th += 1
            lv -= 1
            lh -= 1


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

solution = Solution()
solution.rotate(matrix)
print(matrix)
'''
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

'''
