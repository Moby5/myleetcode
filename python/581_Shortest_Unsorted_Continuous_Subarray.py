#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/05/15/leetcode-shortest-unsorted-continuous-subarray/

LeetCode 581. Shortest Unsorted Continuous Subarray
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

题目大意：
给定一个整数数组，找出其中最短的一段连续子数组，当对这段子数组排序后，整个数组递增有序。

注意：
数组长度范围[1, 10000]
输入数组可能包含重复，因此“递增有序”意思是<=

解题思路：
排序（Sort）
对数组nums排序，记排序后的数组为snums，数组长度为n
令s = e = -1
从0到n-1枚举i，记满足nums[i] != snums[i]的最小i值为s，最大i值为e
则当s != e时，所求最短连续子数组为nums[s .. e]
否则，所求子数组为空
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = sorted(nums)
        low = high = -1
        for i in range(len(nums)):
            if nums[i] != snums[i]:
                if low == -1:
                    low = i
                high = i
        return 0 if low == high else high - low + 1


if __name__ == '__main__':
    solution = Solution()
    print solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
