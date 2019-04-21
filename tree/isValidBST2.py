# -*- coding: utf-8 -*-

#    File Name：       isValidBST
#    Description :
#    Author :          LvYang
#    date：            2019/3/25
#    Change Activity:  2019/3/25:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        print("---------")
        if root is None:
            print("root: {}".format(root))
            return True
        if not self.helper(root.left):
            print("root: {}".format(root))
            return False
        if self.prev and self.prev.val >= root.val:
            print("root: {}".format(root))
            return False
        self.prev = root
        return self.helper(root.right)



def createTree(root):
    if root == None:
        return root

    Root = TreeNode(root[0])
    nodeQueue = [Root]
    index = 1
    front = 0
    while index < len(root):
        node = nodeQueue[front]

        item = root[index]
        index += 1
        if item != None:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(root):
            break

        item = root[index]
        index += 1
        if item != None:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)

        front += 1

    return Root


def printTree(root):
    if root != None:
        printTree(root.left)
        # print(root.val)
        printTree(root.right)


if __name__ == "__main__":
    root = [2, 1, 3]
    treeRoot = createTree(root)
    printTree(treeRoot)
    print(Solution().isValidBST(treeRoot))