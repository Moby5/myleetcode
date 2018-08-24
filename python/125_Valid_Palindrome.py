#!/usr/bin/env python
# coding=utf-8
# Date: 2018-08-24

"""
https://leetcode.com/problems/valid-palindrome/description/

125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = re.sub(r"_|\W", "", s).lower()
        return res == res[::-1]


solution = Solution()
for s in ["A man, a plan, a canal: Panama", "race a car", ""]:
    print(s, solution.isPalindrome(s))

        
