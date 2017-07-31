#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/03/19/leetcode-convert-bst-to-greater-tree/

LeetCode 538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

    Input: The root of a Binary Search Tree like this:
                      5
                                  /   \
                                                     2     13

                                  Output: The root of a Greater Tree like this:
                                               18
                                                           /   \
                                                                     20     13
                                                           题目大意：
                                                           给定一棵二叉查找树（BST），将其转化为“Greater Tree”，原始BST中的每一个节点都替换为不小于其本身的各节点的和。

                                                           解题思路：
                                                           “右 - 根 - 左”顺序遍历BST
"""


class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
        def convertBST(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            def traverse(node):
                if not node:
                    return
                traverse(node.right)
                node.val += self.total
                self.total = node.val
                traverse(node.left)

            self.total = 0
            traverse(root)
            return root
        



