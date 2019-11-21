# -*- coding: utf-8 -*-

#    File Name：       887. Super Egg Drop
#    Description :
#    Author :          LvYang
#    date：            2019/9/16
#    Change Activity:  2019/9/16:
'''
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

你的目标是确切地知道 F 的值是多少。

无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

 

示例 1：

输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
示例 2：

输入：K = 2, N = 6
输出：3
示例 3：

输入：K = 3, N = 14
输出：4
 

提示：

1 <= K <= 100
1 <= N <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-egg-drop
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



K = 3
N = 14
# 输出：4



# class Solution(object):
#     def superEggDrop(self, K, N):
#         """
#         :type K: int
#         :type N: int
#         :rtype: int
#         """
#         dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
#         print(dp)
#         for i in range(1, K + 1):
#             for step in range(1, N + 1):
#                 dp[i][step] = dp[i - 1][step - 1] + (dp[i][step - 1] + 1)
#                 if dp[K][step] >= N:
#                     return step
#         return 0


import numpy as np

def solvepuzzle(n, k):
    numdrops = np.array([[0]*(k+1)]*(n+1))

    for i in range(k+1):
        numdrops[1, i] = i

    for i in range(2, n+1):
        for j in range(1, k+1):
            minimum = float('inf')

            for x in range(1, j+1):
                minimum = min(minimum, (1+max(numdrops[i, j-x], numdrops[i-1, x-1])))

            numdrops[i, j] = minimum

    print(numdrops)
    return numdrops[n,k]



#
# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# so = Solution()
# print(so.superEggDrop(K, N))
print(solvepuzzle(N, K))