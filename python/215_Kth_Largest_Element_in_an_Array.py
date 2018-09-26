#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-26

"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):  # 24 ms
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]
        
    def findKthLargest_v0(self, nums, k):  # 24 ms
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k-1]
        
solution = Solution()
ok = True

nums, k = [3,2,1,5,6,4], 2
if solution.findKthLargest(nums, k) != 5:
    print("测试1不通过")
    ok = False

nums, k = [3,2,3,1,2,4,5,5,6], 4
if solution.findKthLargest(nums, k) != 4:
    print("测试2不通过")   
    ok = False

if ok:
    print("全部测试通过")
    
"""
https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort).
"""

