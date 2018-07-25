#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-25

"""
https://leetcode.com/problems/valid-anagram/description/

242. Valid Anagram  # 同文异位词

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return Counter(s) == Counter(t)
        return sorted(s) == sorted(t)
        
        
