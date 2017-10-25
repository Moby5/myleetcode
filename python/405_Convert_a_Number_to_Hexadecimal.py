#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/09/25/leetcode-convert-a-number-to-hexadecimal/

LeetCode 405. Convert a Number to Hexadecimal

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

IMPORTANT:
You must not use any method provided by the library which converts/formats the number to hex directly. Such solution will result in disqualification of all your submissions to this problem. Users may report such solutions after the contest ends and we reserve the right of final decision and interpretation in the case of reported solutions.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"

题目大意：
将数字转化为16进制字符串，负数采用补码表示。不允许使用系统函数。

解题思路：
进制转换
"""

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = []
        hexs = '0123456789abcdef'
        if num < 10: num += 0x100000000
        while num:
            ans.append(hexs[num % 16])
            num /= 16
        return ''.join(ans[::-1]) if ans else '0'
        

test = Solution()        
nums = [26, -1, 36]
for n in nums:
    print n, test.toHex(n)
        
