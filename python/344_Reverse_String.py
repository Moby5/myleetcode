#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-10

"""
https://leetcode.com/problems/reverse-string/description/

344. Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        
