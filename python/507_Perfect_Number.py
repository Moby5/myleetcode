#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/03/26/leetcode-perfect-number/

题目描述：
LeetCode 507. Perfect Number

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8)

题目大意：
判断某正整数n是否等于除其本身外所有因子之和。

注意：n不超过1e8

解题思路：
模运算
"""

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        total, div = 1, 2
        while div * div <= num:
            if num % div == 0:  
                total += div
                if div * div != num:
                    total += num / div
            div += 1
        return num > 1 and num == total

