#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/08/11/leetcode-ransom-note/

383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

题目大意：
给定两个字符串ransomNote和magazine，编写函数判断magazine中的字符是否可以完全包含ransomNote中的字符。

注意：可以假设字符串中只包含小写字母。

解题思路：
利用Python的collections.Counter类统计字符个数，然后做差即可。
"""

from collections import  Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cr, cm = Counter(ransomNote), Counter(magazine)        
        cm_keys = set(cm.keys())
        for k, v in cr.iteritems():
            if k not in cm_keys or cm[k] < v: return False
        return True
    
    def canConstruct(self, ransomNote, magazine):
        return not Counter(ransomNote) - Counter(magazine)
    
    def canConstruct_ref(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomCnt = collections.Counter(ransomNote)
        magazineCnt = collections.Counter(magazine)
        return not ransomCnt - magazineCnt    
        
solution = Solution()        
print solution.canConstruct("a", "b")  # -> false
print solution.canConstruct("aa", "ab")  # -> false
print solution.canConstruct("aa", "aab")  # -> true

