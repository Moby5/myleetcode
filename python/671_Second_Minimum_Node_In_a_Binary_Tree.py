#!/usr/bin/env python
# coding=utf-8

"""    
    @File: 671_Second_Minimum_Node_In_a_Binary_Tree.py
    @Desc: 
    @Author: Abby Mo
    @Date Created: 2018-3-10
"""

"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. 
If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.

题目大意：
给定一棵二叉树，树中的节点孩子个数为偶数（0个或者2个），若包含2个孩子节点，则值等于较小孩子的值。求树中第二小的节点。
解题思路：
遍历二叉树，记录比根节点大的所有节点中值最小的元素
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or not root.left:
            return -1
        res = self.traverse(root)
        res = sorted(res)
        return res[1] if len(res) >= 2 else -1

    def traverse(self, node):
        if not node:
            return {}
        res = {node.val}
        res.update(self.traverse(node.left))
        res.update(self.traverse(node.right))
        return res

    def findSecondMinimumValue_ref(self, root):  # http://bookshadow.com/weblog/2017/09/03/leetcode-second-minimum-node-in-a-binary-tree/
        self.ans = 0x80000000
        minVal = root.val
        def traverse(root):
            if not root: return
            if self.ans > root.val > minVal:
                self.ans = root.val
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return self.ans if self.ans != 0x80000000 else -1


if __name__ == '__main__':
    solution = Solution()
    n1, n2, n3 = TreeNode(5), TreeNode(8), TreeNode(5)
    n1.left, n1.right = n2, n3
    print solution.findSecondMinimumValue(n1)

