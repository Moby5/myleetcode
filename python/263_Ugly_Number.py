#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/08/19/leetcode-ugly-number/ 

263. Ugly Number

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

题目大意：
编写程序判断一个给定的数字是否为“丑陋数” ugly number

丑陋数是指只包含质因子2, 3, 5的正整数。例如，6, 8是丑陋数而14不是，因为它包含额外的质因子7

注意，数字1也被视为丑陋数

解题思路：
将输入数重复除2, 3, 5，判断得数是否为1即可

时间复杂度：

记num = 2^a * 3^b * 5^c * t，程序执行次数为 a + b + c，换言之，最坏情况为O(log num)
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num = num / x
        return num == 1


test = Solution()
nums = [1, 6, 8, 14]
for num in nums:
    print num, test.isUgly(num)

        
