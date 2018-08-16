#!/usr/bin/env python
# coding=utf-8
# Date: 2018-08-16

"""
https://leetcode.com/problems/merge-sorted-array/description/

88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):  # Accepted
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

    def merge_v2(self, nums1, m, nums2, n):  # Accepted
        nums1[m:] = nums2
        nums1.sort()
        
    def merge_v1(self, nums1, m, nums2, n):  # Accepted
        nums1[:] = sorted(nums1[:m] + nums2[:n])  
        
    def merge_v0(self, nums1, m, nums2, n):  # Wrong Answer : Do not return anything, modify nums1 in-place instead.
        nums1 = sorted(nums1[:m] + nums2[:n])  
    

solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution.merge(nums1, m, nums2, n)
print(nums1)
        
        
"""
https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution

def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
"""            