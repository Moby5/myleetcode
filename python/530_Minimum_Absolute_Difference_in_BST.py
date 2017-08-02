#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/02/26/leetcode-minimum-absolute-difference-in-bst/

题目描述：
LeetCode 530. Minimum Absolute Difference in BST

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:
Input:

   1
       \
                    3
           /
              2
Output:
1

Explanation:
    The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.

题目大意：
给定一棵BST（二叉搜索树），节点值为非负整数，计算任意两节点差的绝对值的最小值。

注意：BST中至少存在两个节点

解题思路：
解法I 中序遍历（In-order Traverse）

中序遍历将BST中的节点按照递增顺序输出
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0x7FFFFFFF
        self.last = -0x80000000  # 记录前一个节点的值
        def inOrderTraverse(node): # 中序遍历(左根右)
            if not node:
                return
            inOrderTraverse(node.left)
            self.ans = min(self.ans, node.val - self.last) # min(当前最小差值, 当前节点的值与前一个节点的差值)
            self.last = node.val  
            inOrderTraverse(node.right)
        inOrderTraverse(root)
        return self.ans


