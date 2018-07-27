#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-27

"""
https://leetcode.com/problems/reverse-linked-list/description/

206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):        
    def reverseList(self, head):  # Iterative
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
        
    def reverseList_v1(self, head):  # Recursive
        """
        :type head: ListNode
        :rtype: ListNode
        """     
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p        
        
    def reverseList_v0(self, head):      
        if not head:
            return head
        nodes = [head]
        while head.next:
            nodes.append(head.next)
            head = head.next
        nodes = nodes[::-1]
        for idx in range(len(nodes) - 1):
            nodes[idx].next = nodes[idx + 1]
        nodes[-1].next = None
        return nodes[0]
