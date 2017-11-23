#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/09/17/leetcode-valid-palindrome-ii/

680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

题目大意：
给定一个非空字符串s，至多删除一个字符。判断是否可以组成回文。

解题思路：
双指针（Two Pointers）

lo, hi分别指向s的左右两侧，向中心移动

当s[lo] != s[hi]时，判断删掉lo或者hi时，剩余字符串是否为回文
"""

class Solution(object):    
    def validPalindrome_v0(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return l
                else:
                    l += 1
                    r -= 1
            return -1
    
        l = isPalindrome(s)
        if l == -1:
            return True
        else:
            r = len(s) - l - 1
            return isPalindrome(s[l+1:r+1]) == -1 or isPalindrome(s[l:r]) == -1            
    
    def validPalindrome(self, s):           
        isPalindrome = lambda s: s == s[::-1]
        
        if isPalindrome(s): return True
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:                
                return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
            l += 1
            r -= 1
        return True
    
    def validPalindrome_ref(self, s):
        isPalindrome = lambda s: s == s[::-1]
        strPart = lambda s, x: s[:x] + s[x + 1:]
        size = len(s)
        lo, hi = 0, size - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return isPalindrome(strPart(s, lo)) or isPalindrome(strPart(s, hi))
            lo += 1
            hi -= 1
        return True               
            
        
solution = Solution()
strs = ["aba", "abca", "abbca", "abbcca", "tcaac"] # t, t, t, f, t
for s in strs:
    print solution.validPalindrome(s)
