#!/usr/bin/env python
# coding=utf-8
"""
http://bookshadow.com/weblog/2017/04/09/leetcode-reverse-words-in-a-string-iii/

LeetCode 557. Reverse Words in a String III

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    Note: In the string, each word is separated by single space and there will not be any extra space in the string.

    题目大意：
    给定字符串，将每个单词逐字符逆置，返回新字符串。

    注意：字符串中单词之间有且只有1个空格分开。

    解题思路：
    字符串处理
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(w[::-1] for w in s.split())


