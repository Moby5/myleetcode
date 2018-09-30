#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-30

"""
https://leetcode.com/problems/increasing-triplet-subsequence/description/

334. Increasing Triplet Subsequence

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:
Input: [1,2,3,4,5]
Output: true

Example 2:
Input: [5,4,3,2,1]
Output: false
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = float('inf'), float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
        

solution = Solution()
assert solution.increasingTriplet([1,2,3,4,5]) == True
assert solution.increasingTriplet([5,4,3,2,1]) == False
assert solution.increasingTriplet([2,1,5,0,4,6]) == True
assert solution.increasingTriplet([5,1,5,5,2,5,4]) == True
print("测试通过")

"""
https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78995/Python-Easy-O(n)-Solution
Start with the maximum numbers for the first and second element. Then:
    (1) Find the first smallest number in the 3 subsequence
    (2) Find the second one greater than the first element, reset the first one if it's smaller
"""

