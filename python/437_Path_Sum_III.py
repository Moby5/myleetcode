#!/usr/bin/env python
# coding=utf-8

"""
437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

题目大意：
给定一颗二叉树，每个节点包含一个整数值。
计算所有和为给定值的路径个数。
路径不一定以根开始，也不一定以叶子结束，但是必须自上而下（从双亲结点到孩子节点）
树节点个数不超过1000，并且节点值的范围在-1,000,000到1,000,000之间。

解题思路：
树的遍历，在遍历节点的同时，以经过的节点为根，寻找子树中和为sum的路径。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum_v0(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def traverse(root, val):
            if not root: return 0
            res = (val == root.val)
            res += traverse(root.left, val - root.val)
            res += traverse(root.right, val - root.val)
            return res
        if not root: return 0
        ans = traverse(root, sum)
        ans += self.pathSum(root.left, sum)
        ans += self.pathSum(root.right, sum)
        return ans

    def pathSum(self, root, sum):
        def traverse(node, val):
            if not node: return 0
            res = 1 if node.val == val else 0
            res += traverse(node.left, val - node.val)
            res += traverse(node.right, val - node.val)
            return res

        if not root: return 0
        ans = traverse(root, sum)
        ans += self.pathSum(root.left, sum)
        ans += self.pathSum(root.right, sum)
        return ans
        
