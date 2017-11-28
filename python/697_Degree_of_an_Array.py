#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/10/15/leetcode-degree-of-an-array/

697. Degree of an Array

Given a non-empty array of non-negative integers nums, 
the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

题目大意：
给定非空非负整数数组，数组的度是指元素的最大出现次数。

寻找最大连续区间，使得区间的度与原数组的度相同。

解题思路：
数组maxs记录元素的最大下标

数组mins记录元素的最小下标

数组cnts记录元素的出现个数

O(n)遍历即可
"""

from collections import Counter, defaultdict

class Solution(object):
    def findShortestSubArray_v0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        size = len(nums)
        nums_inv = nums[::-1]
        min_len = size
        counter = Counter(nums).most_common()        
        max_freq = counter[0][1]                        
        for k, freq in counter:            
            if freq < max_freq: break            
            klen = size - nums_inv.index(k) - nums.index(k)
            if klen < min_len: min_len = klen                
        return min_len
    
    def findShortestSubArray(self, nums):
        indexes = defaultdict(list)
        for idx, n in enumerate(nums):
            indexes[n].append(idx)        
        max_freq = max([len(li) for k, li in indexes.iteritems()])        
        ans = len(nums)
        for k, li in indexes.iteritems():
            if len(li) == max_freq:                 
                klen = max(li) - min(li) + 1                
                if klen < ans:
                    ans = klen                
        return ans
                
    def findShortestSubArray_ref(self, nums):
        mins = {}
        maxs = {}
        cnts = collections.defaultdict(int)
        for idx, num in enumerate(nums):
            maxs[num] = max(maxs.get(num, -1), idx)
            mins[num] = min(mins.get(num, 0x7FFFFFFF), idx)
            cnts[num] += 1
        degree = max(cnts.values())
        ans = len(nums)
        for num in set(nums):
            if cnts[num] == degree:
                ans = min(ans, maxs[num] - mins[num] + 1)
        return ans        
    
    def findShortestSubArray_ref2(self, nums): # https://leetcode.com/problems/degree-of-an-array/solution/
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans    
                
        
solution = Solution()
print solution.findShortestSubArray([1, 2, 2, 3, 1])
print solution.findShortestSubArray([1,2,2,3,1,4,2])
print solution.findShortestSubArray([1,3,2,2,3,1]) # 2

