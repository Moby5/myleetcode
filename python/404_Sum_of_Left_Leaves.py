#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/09/25/leetcode-sum-of-left-leaves/

404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

题目大意：
给定二叉树，计算其所有左叶子的和。

解题思路：
遍历二叉树
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        ans = 0
        queue = [root]
        while queue:
            node = queue.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    ans += node.left.val
                else:
                    queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans
        
    def sumOfLeftLeaves_ref(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if root: 
            l, r = root.left, root.right
            if l and (l.left or l.right) is None:
                ans += l.val
            ans += self.sumOfLeftLeaves(l) + self.sumOfLeftLeaves(r)
        return ans        


test = Solution()
n3, n9, n20, n15, n7 = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
n3.left, n3.right = n9, n20
n20.left, n20.right = n15, n7
print test.sumOfLeftLeaves(n3) # 24

# n1, n2, n3, n4, n5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
# n1.left, n1.right = n2, n3
# n2.left, n2.right = n4, n5
# print test.sumOfLeftLeaves(n1)  # 4
        
