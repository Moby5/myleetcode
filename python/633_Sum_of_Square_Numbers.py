#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/07/02/leetcode-sum-of-square-numbers/

LeetCode 633. Sum of Square Numbers
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: 3
Output: False

题目大意：
给定非负整数c，判断是否存在两个整数a和b，满足a^2 + b^2 = c

解题思路：
在范围[0, int(sqrt(c))]内枚举a，判断c - a^2是否为完全平方数
"""


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(c ** 0.5) + 1):
            b2 = c - a ** 2
            if int(b2 ** 0.5) ** 2 == b2:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    print solution.judgeSquareSum(5)
    print solution.judgeSquareSum(3)
