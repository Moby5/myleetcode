#!/usr/bin/env python
# coding=utf-8
# Date: 2018-10-13

"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):  # 28ms
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, temp, queue, flag = [], [], [root], 1
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp[::flag])
            temp = []
            flag *= -1
        return res
        
    def zigzagLevelOrder_v0(self, root):  # 28 ms
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        queue, order = [[root]], 0
        while queue:
            nodes = queue.pop(0)

            traversal = [node.val for node in nodes]
            if order:
                traversal = traversal[::-1]
            ans.append(traversal)

            new_nodes = []
            for p in nodes:
                if p.left:
                    new_nodes.append(p.left)
                if p.right:
                    new_nodes.append(p.right)
            if new_nodes:
                queue.append(new_nodes)
            order = 0 if order else 1
        return ans


solution = Solution()
nodes = {x: TreeNode(x) for x in [3, 9, 20, 15, 7]}
nodes[3].left, nodes[3].right = nodes[9], nodes[20]
nodes[20].left, nodes[20].right = nodes[15], nodes[7]
expexcted_output = [[3], [20, 9], [15, 7]]
output = solution.zigzagLevelOrder(nodes[3])
assert expexcted_output == output, output
print("ok")

"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33834/Python-simple-BFS
"""

        
