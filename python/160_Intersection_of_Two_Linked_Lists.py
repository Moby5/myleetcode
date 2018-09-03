#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-03

"""
https://leetcode.com/problems/intersection-of-two-linked-lists/description/

160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):  # Two Pointers
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa        

        
    def getIntersectionNode_v0(self, headA, headB):  # Hash Table
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        bag = set()
        while headA:
            bag.add(headA)
            headA = headA.next
        while headB:
            if headB in bag:
                return headB
            headB = headB.next
        return None
        
        
"""
https://leetcode.com/problems/intersection-of-two-linked-lists/solution/

Approach 1: Brute Force
For each node ai in list A, traverse the entire list B and check if any node in list B coincides with ai.

Complexity Analysis
Time complexity : O(mn)O(mn).
Space complexity : O(1)O(1). 


Approach 2: Hash Table
Traverse list A and store the address / reference to each node in a hash set. Then check every node bi in list B: if bi appears in the hash set, then bi is the intersection node.

Complexity Analysis
Time complexity : O(m+n)O(m+n).
Space complexity : O(m)O(m) or O(n)O(n). 


Approach 3: Two Pointers
Maintain two pointers pApA and pBpB initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.
When pApA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pBpB reaches the end of a list, redirect it the head of A.
If at any point pApA meets pBpB, then pApA/pBpB is the intersection node.
To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'. Since B.length (=4) < A.length (=6), pBpB would reach the end of the merged list first, because pBpB traverses exactly 2 nodes less than pApA does. By redirecting pBpB to head A, and pApA to head B, we now ask pBpB to travel exactly 2 more nodes than pApA would. So in the second iteration, they are guaranteed to reach the intersection node at the same time.
If two lists have intersection, then their last nodes must be the same one. So when pApA/pBpB reaches the end of a list, record the last element of A/B respectively. If the two last elements are not the same one, then the two lists have no intersections.

Complexity Analysis
Time complexity : O(m+n)O(m+n).
Space complexity : O(1)O(1).
"""        
