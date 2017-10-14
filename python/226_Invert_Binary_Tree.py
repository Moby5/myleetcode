#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/06/12/leetcode-invert-binary-tree/

226. Invert Binary Tree

Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.

题目大意：
翻转一棵二叉树。

测试样例见题目描述。

花絮：

这道题目的灵感来自于Max Howell的推特原文：

Google：我们90%的工程师在用你写的软件（Homebrew），但你竟然不会在白板上翻转一棵二叉树，所以滚吧。

解题思路：
水题，递归或者队列迭代均可。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """    
        if not root: return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root    
        
    def invertTree_v2(self, root):
        if not root: return root
        queue = [root]
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

    def invertTree_ref(self, root):  # 递归版本
        if root is None:
            return None
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
        
    def invertTree_ref2(self, root):  # 迭代版本
        if root is None:
            return None
        queue = [root]
        while queue:
            front = queue.pop(0)
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
            front.left, front.right = front.right, front.left
        return root        
        
        
