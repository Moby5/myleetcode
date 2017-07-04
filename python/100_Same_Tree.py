#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/08/18/leetcode-same-tree/

LeetCode 100. Same Tree
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

题目大意：
给定两棵二叉树，编写函数检查它们是否相等。
当且仅当两棵二叉树的结构相同并且节点值也相同时，判定为相等。

解题思路：
递归（Recursion）
"""

import argparse


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and \
                       self.isSameTree(p.left, q.left) and \
                       self.isSameTree(p.right, q.right)
        return p is None and q is None


if __name__ == '__main__':
    p = TreeNode(3)
    p.left = TreeNode(1)
    p.right = TreeNode(5)

    # q = TreeNode(4)
    # q.left = TreeNode(2)
    # q.right = TreeNode(6)

    q = TreeNode(3)
    q.left = TreeNode(1)
    # q.right = TreeNode(5)

    # print 'check if the two given binary trees are equal'
    test = Solution()
    print test.isSameTree(p, q)


