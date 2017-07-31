#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/03/12/leetcode-reverse-string-ii/

LeetCode 541. Reverse String II

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:

    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"
    Restrictions:

        The string consists of lower English letters only.
        Length of the given string and k will in the range [1, 10000]
        题目大意：
        给定一个字符串和一个整数k，每2k个字符翻转前k个字符。如果剩余字符不足k个，则全部翻转。如果剩余字符在k到2k之间，则翻转前k个字符，剩余字符保持原样。

        约束条件：

        字符串只包含小写英文字母。
        给定字符串长度和k在范围[1, 10000]之间。
        解题思路：
        字符串模拟
"""

import math
import argparse

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str        
        """
        ans = ''
        round = int(math.ceil(len(s) / (2.0 * k)))
        for r in range(round):
            ans += s[r * 2 * k : (r * 2 + 1) * k][::-1]
            ans += s[(r * 2 + 1) * k : (r * 2 + 2) * k]
        return ans


parser = argparse.ArgumentParser(description='Reverse String II')
parser.add_argument('s', type=str)
parser.add_argument('k', type=int)
args = parser.parse_args()

test = Solution()
# print test.reverseStr('abcdefg', 2)
print test.reverseStr(args.s, args.k)


