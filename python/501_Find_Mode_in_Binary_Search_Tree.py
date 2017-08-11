#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/01/29/leetcode-find-mode-in-binary-tree/

501. Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

题目大意：
给定一棵包含重复元素的二叉树。寻找其中的所有众数。

注意：二叉树可能包含多个众数，以任意顺序返回即可。

解题思路：
二叉树遍历 + 计数
"""

from collections import Counter

# definition for a binary tree node.
class treeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]        
        """
        self.counter = Counter()
        def traverse(node):
            if not node: return
            traverse(node.left)
            self.counter[node.val] += 1
            traverse(node.right)
        traverse(root)
        # maxn = max(counter.values() + [None])
        if len(self.counter) == 0: return []
        maxn = self.counter.most_common()[0][1]        
        return [k for k, v in self.counter.iteritems() if v == maxn]        
    
    def findMode_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        
        self.values = []        
        
        def traverse(node):
            if not node: return            
            traverse(node.left)
            self.values.append(node.val)
            traverse(node.right)
        
        def get_mode(values):
            if not values: return []
            ans = []
            counter = Counter(values)   
            max_count = counter.most_common()[0][1]
            ans = [k for k, v in counter.iteritems() if v == max_count]                  
#             max_count = counter.most_common()[0][1]
#             for k, v in counter.most_common():                
#                 if v == max_count:
#                     ans.append(k)
#                 else: 
#                     break                                          
            return ans

        traverse(root)        
        return get_mode(self.values)    
                

test = Solution()
root = treeNode(1)
node2 = treeNode(2)
node3 = treeNode(2)
root.right = node2
node2.left = node3

print test.findMode(root)
