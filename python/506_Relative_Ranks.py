#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/02/05/leetcode-relative-ranks/

题目描述：
LeetCode 506. Relative Ranks

Given scores of N athletes, find their relative ranks and the men with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:

Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:

N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
题目大意；
给定N名运动员的得分，输出他们的名次。前三名分别输出“金奖”，“银奖”，“铜奖”。

注意：

N是正整数并且不超过10000。
所有运动员的得分是唯一的。
解题思路：
排序（Sort）
"""

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dic = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        dmap = { v : k for k, v in enumerate(sorted(nums, reverse=True)) }
        return [dic[dmap[n]] if dmap[n] <= 2 else str(dmap[n] + 1) for n in nums]


test = Solution()
print test.findRelativeRanks([5, 4, 3, 2, 1])
print test.findRelativeRanks([1, 2, 3, 4, 5])
print test.findRelativeRanks([5, 4, 1, 3, 2])

