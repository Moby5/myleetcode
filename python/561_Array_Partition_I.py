#!/usr/bin/env python
# coding=utf-8
"""
http://bookshadow.com/weblog/2017/04/23/leetcode-array-partition-i/

LeetCode 561. Array Partition I

Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:

Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4.
Note:

n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
题目大意：
给定一个长度为2n的整数数组，将数组分成n组，求每组数的最小值之和的最大值。

注意：

n是正整数，范围[1, 10000]
所有整数范围为[-10000, 10000]
解题思路：
排序（Sort）

将数组从小到大排序，取下标为偶数的元素求和即为答案。
   
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
