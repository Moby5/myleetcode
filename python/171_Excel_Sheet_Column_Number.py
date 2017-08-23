#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2014/12/28/leetcode-excel-sheet-column-number/

171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

题目大意：
相关题目：Excel 表格列标题
给定一个出现在Excel表格中的列标题，返回其对应的列号。

样例如题目描述。

解题思路：
26进制转化为10进制
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for ch in s:
            n = n * 26 + (ord(ch) - ord('A') + 1)
        return n
        

test = Solution()
arr = ['A', 'B', 'C', 'Y', 'Z', 'AA', 'AB'] 
for s in arr:
    print s, test.titleToNumber(s)
