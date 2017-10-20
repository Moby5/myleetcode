#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/07/11/leetcode-lowest-common-ancestor-binary-search-tree/

235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

题目大意：
给定一棵二叉搜索树（BST），寻找BST中两个给定节点的最近公共祖先（LCA）。

根据维基百科对LCA的定义：“节点v与w的最近公共祖先是树T上同时拥有v与w作为后继的最低节点（我们允许将一个节点当做其本身的后继）”

例如，题目描述的样例中，节点2和8的最近公共祖先（LCA）是6。另一个例子，节点2和4的LCA是2，因为根据LCA的定义，一个节点可以是其本身的后继。

解题思路：
根据BST的性质，左子树节点的值＜根节点的值，右子树节点的值＞根节点的值

记当前节点为node，从根节点root出发

若p与q分别位于node的两侧，或其中之一的值与node相同，则node为LCA

否则，若p的值＜node的值，则LCA位于node的左子树

否则，LCA位于node的右子树
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor_v0(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q: return
        queue = [root]
        arr = []
        if p.val > q.val:
            p, q = q, p
        while queue:
            node = queue.pop()
            if p.val <= node.val <= q.val:
                # print p.val, node.val, q.val
                arr.append(node)
            elif q.val < node.val:
                queue.append(node.left)
            else:
                queue.append(node.right)
        for n in arr: print n.val,
        return arr[-1].val

    def lowestCommonAncestor_v1(self, root, p, q):
        node = root
        if p.val > q.val: p, q = q, p
        while node:
            if p.val <= node.val <= q.val:
                return node
            else:
                node = node.left if q.val < node.val else node.right

    def lowestCommonAncestor(self, root, p, q):
        node = root
        if p.val > q.val: p, q = q, p
        while p.val > node.val or q.val < node.val:
            node = node.left if q.val < node.val else node.right
        return node


    def lowestCommonAncestor_ref(self, root, p, q):  # 迭代版本
        while (p.val - root.val) * (q.val - root.val) > 0:
            root = [root.left, root.right][p.val > root.val]
        return root        
        
    def lowestCommonAncestor_ref2(self, root, p, q):  # 递归版本
        if (p.val - root.val) * (q.val - root.val) <= 0:
            return root
        elif p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)        

       
test = Solution()
n0, n2, n3, n4, n5, n6, n7, n8, n9 = TreeNode(0),TreeNode(2), TreeNode(3), TreeNode(4),  TreeNode(5),  TreeNode(6),  TreeNode(7),  TreeNode(8),  TreeNode(9)
n6.left, n6.right = n2, n8
n2.left, n2.right = n0, n4
n8.left, n8.right = n7, n9
n4.left, n4.right = n3, n5
print test.lowestCommonAncestor(n6, n2, n8).val  # 6
print test.lowestCommonAncestor(n6, n2, n4).val  # 2 
print test.lowestCommonAncestor(n6, n2, n7).val  # 6
