#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-12

"""
637. Average of Levels in Binary Tree
DescriptionHintsSubmissionsDiscussSolution
Pick One
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            ans.append(1.0 * sum([node.val for node in queue]) / len(queue))  # type<np.float64> is not supported in leetcode
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return ans


root, n9, n20, n15, n7 = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
root.left, root.right = n9, n20
n20.left, n20.right = n15, n7

solution = Solution()
print solution.averageOfLevels(root)
    
            
        
        
"""
http://bookshadow.com/weblog/2017/07/09/leetcode-average-of-levels-in-binary-tree/

题目大意：
求二叉树每层节点的均值

解题思路：
二叉树层次遍历

class Solution(object):
    def averageOfLevels(self, root):
        ans = []
        que = [root]
        while que:
            ans.append(1.0 * sum([n.val for n in que]) / len(que))
            nque = []
            for n in que:
                if n.left: nque.append(n.left)
                if n.right: nque.append(n.right)
            que = nque
        return ans
"""        
