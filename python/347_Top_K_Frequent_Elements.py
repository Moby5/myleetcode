#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-24

"""
https://leetcode.com/problems/top-k-frequent-elements/description/

347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        return [p[0] for p in counter.most_common(k)]
       
solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))

