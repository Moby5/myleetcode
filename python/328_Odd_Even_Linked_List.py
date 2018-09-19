#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-19

"""
https://leetcode.com/problems/odd-even-linked-list/description/

328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):  # 36 ms
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd, even, even_head = head, head.next, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
        
    def oddEvenList_v0(self, head):  # 56 ms
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        even_head = head.next
        odd, even = head, head.next
        p, nmb = even.next, 3
        while p:
            if nmb % 2 == 1:
                odd.next = p
                odd = p
            else:
                even.next = p
                even = p
            p = p.next
            nmb += 1
        even.next = None
        odd.next = even_head
        return head
                
       
solution = Solution()
for values in [[1, 2, 3, 4, 5], [2, 1, 3, 5, 6, 4, 7]]:
    root = ListNode(values[0])
    node = root
    for x in values[1:]:
        new_node = ListNode(x)
        node.next = new_node
        node = new_node
    solution.oddEvenList(root)
    while(root):
        print(root.val),
        root = root.next    
    print("")


"""
https://leetcode.com/problems/odd-even-linked-list/solution/
Intuition

Put the odd nodes in a linked list and the even nodes in another. Then link the evenList to the tail of the oddList.

Algorithm

The solution is very intuitive. But it is not trivial to write a concise and bug-free code.

A well-formed LinkedList need two pointers head and tail to support operations at both ends. The variables head and odd are the head pointer and tail pointer of one LinkedList we call oddList; the variables evenHead and even are the head pointer and tail pointer of another LinkedList we call evenList. The algorithm traverses the original LinkedList and put the odd nodes into the oddList and the even nodes into the evenList. To traverse a LinkedList we need at least one pointer as an iterator for the current node. But here the pointers odd and even not only serve as the tail pointers but also act as the iterators of the original list.

The best way of solving any linked list problem is to visualize it either in your mind or on a piece of paper. An illustration of our algorithm is following:

Illustration of odd even linked list

Figure 1. Step by step example of the odd and even linked list.

public class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) return null;
        ListNode odd = head, even = head.next, evenHead = even;
        while (even != null && even.next != null) {
            odd.next = even.next;
            odd = odd.next;
            even.next = odd.next;
            even = even.next;
        }
        odd.next = evenHead;
        return head;
    }
}

Complexity Analysis

Time complexity : O(n)O(n). There are total nn nodes and we visit each node once.

Space complexity : O(1)O(1). All we need is the four pointers.
"""

