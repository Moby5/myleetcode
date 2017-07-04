#!/usr/bin/env python
# coding=utf-8
"""
[LeetCode] 111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

题目大意：
给定一棵二叉树，计算其最小深度。
最小深度是指从根节点出发到达最近的叶子节点所需要经过的节点个数。

解题思路：
DFS或者BFS均可，详见代码。
"""

import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # DFS
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left and right:
            return min(left, right) + 1
        return max(left, right) + 1

    # BFS
    def minDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, step = queue.popleft()
            if not node.left and not node.right:
                return step
            if node.left:
                queue += (node.left, step + 1),  # 注意逗号
            if node.right:
                queue += (node.right, step + 1),


