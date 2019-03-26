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
        inorder = self.inorder(root)
        print(inorder)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


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
    root = [2, 1, 3, 4,6,8]
    treeRoot = createTree(root)
    printTree(treeRoot)
    print(Solution().isValidBST(treeRoot))