# -*- coding: utf-8 -*-

#    File Name：       reverseList
#    Description :
#    Author :          LvYang
#    date：            2019/3/21
#    Change Activity:  2019/3/21:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head

        while cur != None:
            print("--------")
            lat = cur.next
            cur.next = pre
            pre = cur
            cur = lat
            printList(cur)

            printList(pre)


        return pre


def createList():
    head = ListNode(0)
    cur = head
    for i in range(1, 10):
        cur.next = ListNode(i)
        cur = cur.next
    return head


def printList(head):
    cur = head
    while cur != None:
        print(cur.val, '-->', end='')
        cur = cur.next

    print('NULL')


if __name__ == "__main__":
    head = createList()
    printList(head)
    res = Solution().reverseList(head)
    printList(res)
