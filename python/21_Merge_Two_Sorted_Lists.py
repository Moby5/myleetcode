#!/usr/bin/env python
# coding=utf-8
# Date: 2018-08-01

"""
https://leetcode.com/problems/merge-two-sorted-lists/description/

21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):  # recursively
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
    def mergeTwoLists_v1(self, l1, l2):  # iteratively
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        last = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                last.next = l1
                l1 = l1.next
            else:
                last.next = l2
                l2 = l2.next
            last = last.next
        last.next = l1 or l2
        return dummy.next
        
    def mergeTwoLists_v0(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        last = l1
        p1, p2 = l1.next, l2
        while p1 and p2:
            if p1.val <= p2.val:                
                last.next = p1
                last, p1 = p1, p1.next
            else:
                last.next = p2
                last, p2 = p2, p2.next
        if not p1:
            last.next = p2
        elif not p2:
            last.next = p1                
        return l1

n1, n2, n4 = ListNode(1), ListNode(2), ListNode(4)
n21, n23, n24 = ListNode(1), ListNode(3), ListNode(4)
n1.next, n2.next = n2, n4
n21.next, n23.next = n23, n24

solution = Solution()
ans = solution.mergeTwoLists(n1, n21)
while ans:
    print(ans.val)
    ans = ans.next

        
"""
# iteratively
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
    
# recursively    
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
        
# in-place, iteratively        
def mergeTwoLists(self, l1, l2):
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
"""        
        
