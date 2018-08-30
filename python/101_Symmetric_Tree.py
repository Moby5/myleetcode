#!/usr/bin/env python
# coding=utf-8
# Date: 2018-08-30

"""
https://leetcode.com/problems/symmetric-tree/description/

101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):  # Iterative
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root, root]
        while queue:
            t1, t2 = queue.pop(), queue.pop()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            queue.extend([t1.left, t2.right, t1.right, t2.left])
        return True
        

"""
https://leetcode.com/problems/symmetric-tree/solution/

Approach 1: Recursive
A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
Therefore, the question is: when are two trees a mirror reflection of each other?

Two trees are a mirror reflection of each other if:
Their two roots have the same value.
The right subtree of each tree is a mirror reflection of the left subtree of the other tree.

Complexity Analysis:
Time complexity : O(n)O(n). Because we traverse the entire input tree once, the total run time is O(n)O(n), where nn is the total number of nodes in the tree.
Space complexity : The number of recursive calls is bound by the height of the tree. In the worst case, the tree is linear and the height is in O(n)O(n). Therefore, space complexity due to recursive calls on the stack is O(n)O(n) in the worst case. 

class Solution(object):
    def isSymmetric(self, root):
        return self.is_mirror(root, root)

    def is_mirror(self, t1, t2):   # Recursive
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and self.is_mirror(t1.left, t2.right) and self.is_mirror(t1.right, t2.left)


Approach 2: Iterative
Instead of recursion, we can also use iteration with the aid of a queue. Each two consecutive nodes in the queue should be equal, and their subtrees a mirror of each other. Initially, the queue contains root and root. Then the algorithm works similarly to BFS, with some key differences. Each time, two nodes are extracted and their values compared. Then, the right and left children of the two nodes are inserted in the queue in opposite order. The algorithm is done when either the queue is empty, or we detect that the tree is not symmetric (i.e. we pull out two consecutive nodes from the queue that are unequal).

Complexity Analysis
Time complexity : O(n)O(n). Because we traverse the entire input tree once, the total run time is O(n)O(n), where nn is the total number of nodes in the tree.
Space complexity : There is additional space required for the search queue. In the worst case, we have to insert O(n)O(n) nodes in the queue. Therefore, space complexity is O(n)O(n).

class Solution(object):
    def isSymmetric(self, root):  # Iterative
        queue = [root, root]
        while queue:
            t1, t2 = queue.pop(), queue.pop()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            queue.extend([t1.left, t2.right, t1.right, t2.left])
        return True
"""        
                      

