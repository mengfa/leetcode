# -*- coding: utf-8 -*-

#    File Name：       703
#    Description :
#    Author :          LvYang
#    date：            2019/3/28
#    Change Activity:  2019/3/28:
import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = nums
        self.size = len(self.pool)
        self.k = k
        # heapq.heapify()将列表原地转换为堆并排序
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

k = 3
arr = [4,5,8,2]
kthLargest = KthLargest(3, arr)
kthLargest.add(3)
kthLargest.add(5)
kthLargest.add(10)
kthLargest.add(9)
kthLargest.add(4)