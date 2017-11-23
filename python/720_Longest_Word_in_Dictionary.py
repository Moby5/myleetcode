#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/11/05/leetcode-longest-word-in-dictionary/

720. Longest Word in Dictionary

Given a list of strings words representing an English Dictionary, 
find the longest word in words that can be built one character at a time by other words in words. 
If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. 
However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].

题目大意：
给定一组词组成的字典，判断其中前缀均可以在字典中找到的最长词，若存在长度相同的情况，则返回字典序最小的词。

解题思路：
排序 + 字典
"""

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """        
        ans = ''
        wset = set([''])
        for w in sorted(words):
            if w[:-1] in wset:
                wset.add(w)
                if len(w) > len(ans):
                    ans = w
        return ans                      
        
        
solution = Solution()        
words = ["w","wo","wor","worl", "world"]
print solution.longestWord(words)
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print solution.longestWord(words)
words = ["a", "b", "ba", "banana", "app", "appl", "ap", "apply", "apple"]
print solution.longestWord(words)
