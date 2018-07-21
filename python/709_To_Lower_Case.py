#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-21

"""
https://leetcode.com/problems/to-lower-case/description/

709. To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()
        
