#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/10/09/leetcode-add-strings/

415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

题目大意：
给定两个以字符串表示的非负整数num1, num2，返回num1与num2的和。

注意：

num1和num2的长度< 5100
num1和num2只包含数字0-9
num1和num2不包含前导0
你不能使用内置的BigInteger库，也不能直接把输入转换为整数。

解题思路：
模拟大数加法，注意进位即可。
"""

class Solution(object):
    def addStrings_chick(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = int(num1), int(num2)
        return str(n1 + n2)

    def addStrings(self, num1, num2):
        res = []
        idx1, idx2 = len(num1), len(num2)
        carry = 0
        while idx1 or idx2 or carry:
            digit = carry
            if idx1:
                idx1 -= 1
                digit += int(num1[idx1])
            if idx2:
                idx2 -= 1
                digit += int(num2[idx2])
            carry = digit > 9
            res.append(str(digit % 10))
        return ''.join(res[::-1])

    def addStrings_reference(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        carry = 0
        idx1, idx2 = len(num1), len(num2)
        while idx1 or idx2 or carry:
            digit = carry
            if idx1:
                idx1 -= 1
                digit += int(num1[idx1])
            if idx2:
                idx2 -= 1
                digit += int(num2[idx2])
            carry = digit > 9
            result.append(str(digit % 10))
        return ''.join(result[::-1])        

test = Solution()        
print test.addStrings("10", "21")
        
