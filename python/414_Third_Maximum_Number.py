#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/10/09/leetcode-third-maximum-number/

414. Third Maximum Number

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

题目大意：
给定一个整数数组，返回数组中第3大的数，如果不存在，则返回最大的数字。时间复杂度应该是O(n)或者更少。

解题思路：
利用变量a, b, c分别记录数组第1,2,3大的数字
遍历一次数组即可，时间复杂度O(n)
"""

import numpy as np

class Solution(object):
    def thirdMax(self, nums): 
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b, c = None, None, None
        for n in nums:
            if n > a:
                a, b, c = n, a, b
            elif a > n > b:
                b, c = n, b
            elif b > n > c:
                c = n
        return c if c is not None else a  # 不能直接 return c if c else a　因为c可能为0
        
    def thirdMax_runtime_error(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ns = np.unique(nums)
        return np.max(ns) if len(ns) < 3 else ns[-3]

    def thirdMax_ref(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = c = None
        for n in nums:
            if n > a:
                a, b, c = n, a, b
            elif a > n > b:
                b, c = n, b
            elif b > n > c:
                c = n
        return c if c is not None else a        

test = Solution()        
print test.thirdMax([3,2,1])
print test.thirdMax([1,2])
print test.thirdMax([2,2,3,1])
print test.thirdMax([3,3,4,3,4,3,0,3,3])

