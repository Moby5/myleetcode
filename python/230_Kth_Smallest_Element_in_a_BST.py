#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-18

"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cnt = []
        self.helper(root, cnt, k)
        return cnt[k - 1]

    def helper(self, node, cnt, k):
        if not node:
            return None
        self.helper(node.left, cnt, k)
        cnt.append(node.val)
        if len(cnt) == k:  # 56 ms  <= 96ms
            return None
        self.helper(node.right, cnt, k)
        
    def kthSmallest_v0(self, root, k):  # 52 ms
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        x = 1
        while stack and x <= k:
            node = stack.pop()
            x += 1
            right = node.right
            while right:
                stack.append(right)
                right = right.left
        return node.val
        
"""
http://bookshadow.com/weblog/2015/07/02/leetcode-kth-smallest-element-bst/

给定一棵二叉搜索树（BST），编写一个函数kthSmallest找出其中第k小的元素。

注意：
你可以假设k总是有效的， 1 ≤ k ≤ BST的元素总数。

进一步思考：
如果BST的修改（插入/删除）操作十分频繁，并且需要频繁地找出第k小的元素，应该怎样优化kthSmallest函数？


提示：

尝试利用BST的属性。

如果你可以修改BST节点的结构时，应该怎样做？

最优时间复杂度应该是O(BST的高度)。

解题思路：
BST具有如下性质：

左子树中所有元素的值均小于根节点的值

右子树中所有元素的值均大于根节点的值

因此采用中序遍历（左 -> 根 -> 右）即可以递增顺序访问BST中的节点，从而得到第k小的元素，时间复杂度O(k)



进一步思考：
如果BST节点TreeNode的属性可以扩展，则再添加一个属性leftCnt，记录左子树的节点个数

记当前节点为node
当node不为空时循环：
若k == node.leftCnt + 1：则返回node
否则，若k > node.leftCnt：则令k -= node.leftCnt + 1，令node = node.right
否则，node = node.left

上述算法时间复杂度为O(BST的高度)
"""        

"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63660/3-ways-implemented-in-JAVA-(Python):-Binary-Search-in-order-iterative-and-recursive
"""


