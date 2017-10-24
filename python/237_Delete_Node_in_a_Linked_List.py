#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/07/15/leetcode-delete-node-linked-list/

237. Delete Node in a Linked List

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

题目大意：
编写一个函数删除单链表中（除末尾节点外）的一个节点，只提供待删除节点。

假如链表是1 -> 2 -> 3 -> 4 给你第3个节点，值为3，则调用你的函数后链表为1 -> 2 -> 4 

解题思路：
链表基本操作，记待删除节点为node

令node.val = node.next.val，node.next = node.next.next即可
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
        
