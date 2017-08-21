#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2014/12/20/leetcode-excel-sheet-column-title/

168. Excel Sheet Column Title

题目描述：
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    
题目大意：
给定一个正整数，返回其在Excel表格中对应的列标题。

样例如上。

解题思路：
简单题。可以理解为进制转化，将10进制数转化为每位以A-Z表示的26进制数。

使用Python解题时，需要使用ord()函数将字母转化为整数，使用chr()函数将整数转化回字母。    
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n:            
            ans = chr(ord('A') + (n-1) % 26) + ans
            n = (n-1) / 26
        return ans
    

test = Solution()
for n in range(55):
    print test.convertToTitle(n)    
