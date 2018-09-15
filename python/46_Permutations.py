#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-15

"""
https://leetcode.com/problems/permutations/description/

46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):
    def permute(self, nums):  # 44 ms
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        ans = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for y in self.permute(n):
                ans.append([num] + y)
        return ans


solution = Solution()
print(solution.permute([1,2,3]))


"""
http://bookshadow.com/weblog/2016/09/09/leetcode-permutations/

题目大意：
给定一个唯一数字的集合，返回所有可能的排列。

测试用例如题目描述。

解题思路：
递归（Recursion）

记传入数组为nums，若nums的长度不大于1，则直接返回[nums]

遍历nums，从中抽取一个数num，递归计算剩余数字组成的数组n，然后将num与结果合并

更多种解法参考（Java）：
https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)
"""
        
