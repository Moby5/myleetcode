#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/07/10/leetcode-palindrome-linked-list/

234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

题目大意：
给定一个单链表，判断它是否是回文。

进一步思考：

你可以在O(n)时间复杂度和O(1)空间复杂度完成吗？

解题思路：
1). 使用快慢指针寻找链表中点

2). 将链表的后半部分就地逆置，然后比对前后两半的元素是否一致

3). 恢复原始链表的结构（可选）
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        if len(arr) <= 1: return True
        mid = len(arr) / 2
        print arr[:mid], arr[-mid:][::-1]
        return arr[:mid] == arr[-mid:][::-1]
        
    def isPalindrome_ref(self, head):
        if head is None:
            return True
        #find mid node
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #reverse second half
        p, last = slow.next, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        #check palindrome
        p1, p2 = last, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
        #resume linked list(optional)
        p, last = last, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        slow.next = last
        return p1 is None        
        

test = Solution()
n0 = ListNode(1)
# n1 = ListNode(2)
# n2 = ListNode(3)
# n3 = ListNode(3)
# n4 = ListNode(2)
# n5 = ListNode(2)
# n0.next = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
print test.isPalindrome(n0)
