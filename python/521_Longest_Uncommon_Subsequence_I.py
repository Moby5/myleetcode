#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/04/03/leetcode-longest-uncommon-subsequence-i/

LeetCode 521. Longest Uncommon Subsequence I

Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc"
Output: 3
Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
because "aba" is a subsequence of "aba", 
but not a subsequence of any other strings in the group of two strings. 

Note:

Both strings' lengths will not exceed 100.
Only letters from a ~ z will appear in input strings.
题目大意：
给定两个字符串，计算其“最长不公共子序列”。最长不公共子序列是指：两字符串中某一个的子序列，该子序列不是另一个字符串的子序列，并且长度最长。

子序列是指从一个序列中删除一些字符，剩余字符顺序保持不变得到的新序列。任何字符串都是其本身的子序列，空串不属于任意字符串的子序列。

返回最长不公共子序列，若不存在，返回-1。

注意：

两字符串长度均不超过100
输入字符串只包含小写字母a-z
解题思路：
若两字符串不相等，选择较长的字符串返回长度即可。

否则返回-1。（若两字符串相等，则任意字符串的子串均为另一个的子串）
"""

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if (a == b) else max(len(a), len(b))       
        # return (a != b) and max(len(a, len(b))) or -1

