#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/10/01/leetcode-longest-univalue-path/

687. Longest Univalue Path

Given a binary tree, find the length of the longest path where each node in the path has the same value. 
This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

题目大意：
给定二叉树，求节点值全部相等的最长路径。路径不一定要通过树根。

解题思路：
递归（Recursion）
"""

# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
class Solution(object):   
    def longestUnivaluePath(self, root): # ref
        """
        :type root: TreeNode
        :rtype: int        
        """            
        def longestPath(root, val):
            if not root or root.val != val: return 0
            return 1 + max(longestPath(root.left, val), longestPath(root.right, val))         
        
        if not root: return 0
        left, right, val = root.left, root.right, root.val
        return max(longestPath(left, val) + longestPath(right, val), 
                   self.longestUnivaluePath(left), self.longestUnivaluePath(right))
    
    def longestUnivaluePath_ref2(self, root):  # Recursion https://leetcode.com/problems/longest-univalue-path/solution/
        self.ans = 0
        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans    
   

    
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5    
# n5 = TreeNode(5)            
# n4 = TreeNode(4)
# n5_2 = TreeNode(5)
# n1_3l, n1_3r = TreeNode(1), TreeNode(1)
# n5_3 = TreeNode(5)
# n5.left, n5.right = n4, n5_2
# n4.left, n4.right = n1_3l, n1_3r
# n5_2.right = n5_3
# solution = Solution()
# print solution.longestUnivaluePath(n5)  # 2
        
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5    
# n1 = TreeNode(1)
# n4_2l, n4_3l, n4_3r = TreeNode(4), TreeNode(4), TreeNode(4)
# n5_2r, n5_3r = TreeNode(5), TreeNode(5)
# n1.left, n1.right = n4_2l, n5_2r
# n4_2l.left, n4_2l.right = n4_3l, n4_3r
# n5_2r.right = n5_3r
# solution = Solution()
# print solution.longestUnivaluePath(n1)  # 2

#                 1
#              /     \
#             2       2
#            / \     / \
#           2   2   2   2
#          /
#         2
# n1 = TreeNode(1)
# n2_2l, n2_2r = TreeNode(2), TreeNode(2)
# n2_3ll, n2_3lr, n2_3rl, n2_3rr = TreeNode(2), TreeNode(2), TreeNode(2), TreeNode(2)
# n2_4l = TreeNode(2)
# n1.left, n1.right = n2_2l, n2_2r
# n2_2l.left, n2_2l.right = n2_3ll, n2_3lr
# n2_2r.left, n2_2r.right = n2_3rl, n2_3rr
# n2_3ll.left = n2_4l
# solution = Solution()
# print solution.longestUnivaluePath(n1)  # 3

