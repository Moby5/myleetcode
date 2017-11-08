#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/08/21/leetcode-first-unique-character-in-a-string/

LeetCode 387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

题目大意：
给定一个字符串，寻找第一个不重复字符并返回其下标。如果不存在，返回-1。

注意：你可以假设字符串只包含小写字母。

解题思路：
首先统计每个字符的出现次数，然后遍历一次原字符串。
"""

from collections import Counter

class Solution(object):
    def firstUniqChar_v0(self, s):
        """
        :type s: str
        :rtype: int
        """
        for idx, ch in enumerate(s):
            # print idx, ch, s[idx+1:], s[idx+1:].find(ch)
            if s[idx+1:].find(ch) == -1 and s[:idx].find(ch) == -1:
                return idx
        return -1
    
    def firstUniqChar(self, s):
        counter = Counter(s)
        # print counter
        for idx, ch in enumerate(s):
            if counter[ch] == 1:
                return idx
        return -1
        
        
test = Solution()
strs = ['leetcode', 'loveleetcode', 'cc']  # 0, 2, -1
for s in strs:
    print test.firstUniqChar(s)
