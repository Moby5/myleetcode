#!/usr/bin/env python
# coding=utf-8

"""
LeetCode 532. K-diff Pairs in an Array

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:

The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
题目大意：
给定一个整数数组nums，以及一个整数k，找出其中所有差恰好为k的不重复数对。

注意：

数对(i, j) 和 (j, i)算作同一个数对
数组长度不超过10,000
所有整数在范围[-1e7, 1e7]之间
解题思路：
字典（Map）

首先将nums中的数字放入字典c

遍历set(nums)，记当前数字为n

若n + k在c中，则将结果+1
"""

import argparse
import collections

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int        
        """
        if k < 0:
            return 0
        c = collections.Counter(nums)
        thres = 0 if k else 1
        return sum(c[n+k] > thres for n in c.keys())
        # return sum(c[n+k] > 1 - bool(k) for n in c.keys())

    def findPairs_2(self, nums, k):  # Time Limit Exceeded
        """
        :type nums: List[int]
        :type k: int
        :rtype: int        
        """
        if k < 0:
            return 0
        ans = set()
        arr = sorted(nums)
        # print 'arr:', arr        
        for i in range(len(arr) - 1):            
            if arr[i] not in ans and (arr[i] + k) in arr[i+1:]:
                # print arr[i], arr[i+1:]
                ans.add(arr[i])
        return len(ans)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='find k-diff pairs in an array')
    parser.add_argument('-nums', type=int, nargs='+')
    parser.add_argument('-k', type=int)
    args = parser.parse_args()

    test = Solution()
    print test.findPairs(args.nums, args.k)
    




