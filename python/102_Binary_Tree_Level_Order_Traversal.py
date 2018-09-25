#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-25

"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict

class Solution(object):
    def levelOrder(self, root):  # 32 ms
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.ans = defaultdict(list)
        self.traverse(0, root)
        return [item[1] for item in sorted(self.ans.items(), key=lambda x: x[0])]

        
    def traverse(self, height, node):
        if not node:
            return None
        self.ans[height].append(node.val)
        self.traverse(height + 1, node.left)
        self.traverse(height + 1, node.right)
            

