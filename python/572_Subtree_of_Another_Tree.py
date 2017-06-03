#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/05/07/leetcode-subtree-of-another-tree/

LeetCode 572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:

   4
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:

   4
  / \
 1   2

Return false.

题目大意：
给定两个非空二叉树s和t，判断t是否是s的子树。s的子树是指由s中某节点及该节点的所有子节点构成的二叉树。
特别的，s是其本身的子树。

解题思路：
嵌套遍历二叉树
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return not s and not t
        if self.check(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def check(self, s, t):
        if not s or not t:
            return not s and not t
        if s.val != t.val:
            return False
        return self.check(s.left, t.left) and self.check(s.right, t.right)


# class Solution(object):
#     def isSubtree(self, s, t):
#         """
#         :type s: TreeNode
#         :type t: TreeNode
#         :rtype: bool
#         """
#         if not s or not t:
#             return not s and not t
#         if s.val == t.val and self.isSubtree(s.left, t.left) and self.isSubtree(s.right, t.right):
#             return True
#         else:
#             return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


if __name__ == '__main__':
    # solution = Solution()
    pass
