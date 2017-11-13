#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/10/05/leetcode-word-pattern/

290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

题目大意：
给定一个模式pattern和一个字符串str，判断str是否满足相同的pattern。

测试用例如题目描述。

注意：

pattern和str都只包含小写字母。
pattern和str不包含前导或者后缀空格。
str中的每一个单词之间都由一个空格分开。
pattern中的每一个字母都对应一个长度至少为1的单词。

解题思路：
使用字典dict分别记录pattern到word的映射以及word到pattern的映射

这道题和题目Isomorphic Strings十分类似
"""

from collections import defaultdict

class Solution(object):
    def wordPattern_v0(self, pattern, strs):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = defaultdict(list)
        strs = strs.split(' ')
        size = len(strs)
        if len(pattern) != size: return False
        for idx, p in enumerate(pattern):
            d[p].append(idx)             
        visited = set()
        for k, v in d.iteritems():            
            idx_orig = v[0]
            if idx_orig >= size: return False
            if strs[idx_orig] in visited:
                return False
            visited.add(strs[idx_orig])
            for idx in v[1:]:
                if idx >= size: return False
                if strs[idx] != strs[idx_orig]:
                    return False
        return True
    
    def wordPattern(self, pattern, strs):  # _ref
        words = strs.split(' ')
        if len(pattern) != len(words):
            return False
        ptn_dict, word_dict = {}, {}
        for ptn, word in zip(pattern, words):
            if ptn not in ptn_dict:
                ptn_dict[ptn] = word
            if word not in word_dict:
                word_dict[word] = ptn
            if ptn_dict[ptn] != word or word_dict[word] != ptn:
                return False
        return True   
        
        
solution = Solution()
print solution.wordPattern("abba", "dog cat cat dog")  # True
print solution.wordPattern("abba", "dog cat cat fish") # False
print solution.wordPattern("aaaa", "dog cat cat dog")  # False
print solution.wordPattern("abba", "dog dog dog dog")  # False
print solution.wordPattern("aaa", "aa aa aa aa")  # False
