#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/02/12/leetcode-base-7/

题目描述：
LeetCode 504. Base 7

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"

Example 2:

Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].

题目大意：
给定一个整数，返回其7进制的字符串。

注意： 输入在范围[-1e7, 1e7]之内。

解题思路：
进制转换
"""

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        n = abs(num)
        while n:
            ans += str(n % 7)
            n /= 7
        return ['', '-'][num < 0] + ans[::-1] or '0'
#        return '0' if num == 0 else ('' if num > 0 else '-') + ans[::-1]
        
#        ans = ''
#        prefix = '-' if num < 0 else ''
#        num = abs(num)
#        if num == 0:
#            return '0'
#        while num > 0:
#            ans += str(num % 7)
#            num /= 7    
#        return prefix + ans[::-1]


test = Solution()
print test.convertToBase7(100)
print test.convertToBase7(-7)
print test.convertToBase7(0)

