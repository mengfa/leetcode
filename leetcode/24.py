# -*- coding: utf-8 -*-

#    File Name：       24
#    Description :
#    Author :          LvYang
#    date：            2019-12-15
#    Change Activity:  2019-12-15:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createList():
    head = ListNode(1)
    cur = head

    for i in range(2, 5):
        cur.next = ListNode(i)
        cur = cur.next
    return head


def printList(head):
    cur = head
    while cur != None:
        print(cur.val, '-->', end='')
        cur = cur.next
    print('NULL')


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(-1)
        h.next = head
        pre = h
        while pre.next != None and pre.next.next != None:
            node1 = pre.next
            node2 = node1.next
            lat = node2.next

            pre.next = node2
            node2.next = node1
            node1.next = lat

            pre = node1

        return h.next


if __name__ == "__main__":
    head = createList()
    printList(head)
    res = Solution().swapPairs(head)
    printList(res)
