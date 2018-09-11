#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-11

"""
https://leetcode.com/problems/subsets/description/

78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        res = []
        for sets in self.subsets(nums[1:]):
            res.extend([sets])
            res.extend([[nums[0]] + sets])
        return res

solution = Solution()
for nums in [[1, 2, 3]]:
    print(nums, solution.subsets(nums))
        
