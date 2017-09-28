#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/12/04/leetcode-number-of-words-in-a-string/

434. Number of Segments in a String

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5

题目大意：
计算字符串中的非空子串的个数。

解题思路：
用内置函数split即可
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
        
test = Solution()
print test.countSegments("Hello, my name is John")
        
