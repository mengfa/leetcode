# -*- coding: utf-8 -*-

#    File Name：       searchMatix
#    Description :
#    Author :          LvYang
#    date：            2019/9/11
#    Change Activity:  2019/9/11:


# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if not matrix:
#             return False
#         rows = len(matrix)
#         cols = len(matrix[0]) - 1
#         row = 0
#         while row < rows and cols >= 0:
#             print("matrix[row][cols]: {}, target: {}".format(matrix[row][cols], target))
#             if matrix[row][cols] == target:
#                 return True
#             elif matrix[row][cols] > target:
#                 cols -= 1
#             else:
#                 row += 1
#         return False

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])-1
        row = 0
        while row < rows and cols >=0:
            if matrix[row][cols] == target:
                return True
            elif matrix[row][cols] > target:
                cols -= 1
            else:
                row += 1






# input = [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
input = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 18

so = Solution()
output = so.searchMatrix(input, target)
print(output)
