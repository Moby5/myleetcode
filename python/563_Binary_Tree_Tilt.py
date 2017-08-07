#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/04/23/leetcode-binary-tree-tilt/

题目描述：
LeetCode 563. Binary Tree Tilt

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
                /   \
                      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1

Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
题目大意：
给定二叉树，计算二叉树的“倾斜值”（tilt）

二叉树节点的倾斜值是指其左右子树和的差的绝对值。空节点的倾斜值为0。

注意：

节点和不超过32位整数范围
倾斜值不超过32位整数范围
解题思路：
遍历二叉树 + 递归求二叉树子树和
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def traverse(node):
            if not node:
                return 0
            left_sum = traverse(node.left)
            right_sum = traverse(node.right)
            # print node.val, left_sum, right_sum
            self.ans += abs(left_sum - right_sum)
            return node.val+ left_sum + right_sum
        traverse(root)
        return self.ans


if __name__ == '__main__':
    #root = TreeNode(1)
    #root.left = TreeNode(2)
    #root.right = TreeNode(3)
    
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)   
    node5 = TreeNode(5)

    root.left = node2
    root.right = node3
    node2.left = node4
    node3.right = node5
    test = Solution()
    print test.findTilt(root)
