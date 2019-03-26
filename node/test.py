# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """


        new_head = ListNode(0)
        new_head.next = head
        fast = slow = new_head
        for i in range(n + 1):
            fast = fast.next
            print(fast, fast.val)
        while fast:
            fast = fast.next
            slow = slow.next
            # print("fast val: {}, slow val: {}".format(fast.val, slow.val))
        print(slow.val)
        slow.next = slow.next.next
        return new_head.next




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
    res = Solution().removeNthFromEnd(head, 2)
    printList(res)