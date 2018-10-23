#!/usr/bin/env python
# coding=utf-8
# Date: 2018-10-23
# File: 148_Sort_List.py

"""
https://leetcode.com/problems/sort-list/

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):  # 归并排序 200 ms
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        mid = self._getMiddle(head)
        rHead = mid.next
        mid.next = None
        return self._merge(self.sortList(head), self.sortList(rHead))
        
    def _merge(self, lHead, rHead):
        dummyNode = ListNode(0)
        dummyHead = dummyNode
        while lHead and rHead:
            if lHead.val < rHead.val:
                dummyHead.next = lHead
                lHead = lHead.next
            else:
                dummyHead.next = rHead
                rHead = rHead.next
            dummyHead = dummyHead.next
        if lHead:
            dummyHead.next = lHead
        elif rHead:
            dummyHead.next = rHead
        return dummyNode.next

    def _getMiddle(self, head):
        if head is None:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def sortList_v0(self, head):  # 值排序 120 ms
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        values, node = [], head
        while node:
            values.append(node.val)
            node = node.next
        values = sorted(values)
        res = [ListNode(v) for v in values]
        for i in range(len(res) - 1):
            res[i].next = res[i+1]
        return res[0]

solution = Solution()

Input = [ListNode(v) for v in [4,2,1,3]]
for i in range(len(Input) - 1):
    Input[i].next = Input[i+1]
expected_output = [1,2,3,4]
Output = solution.sortList(Input[0])
output, node = [], Output
while node:
    output.append(node.val)
    node = node.next
assert expected_output == output, output

print("Pass.")

"""
http://bookshadow.com/weblog/2014/11/21/leetcode-sort-list/

题目大意：
使用常数空间复杂度，对一个链表执行O(n log n）时间复杂度的排序

解题思路：
归并排序，链表的中点可以通过“快慢指针”法求得。
"""
