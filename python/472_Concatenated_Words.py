#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/12/18/leetcode-concatenated-words/

LeetCode 472. Concatenated Words

Given a list of words, please write a program that returns all concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:

Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:

The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
The returned elements order does not matter.
题目大意：
给定一组单词，编写程序返回所有由别的单词拼接而成的单词。

拼接是指至少由给定数组中的两个更短的单词组合。

注意：

数组长度不会超过10000
单词总长度不会超过600000
返回结果的顺序无所谓
解题思路：
解法I 深度优先搜索（Depth First Search）
"""

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        self.word_set = set(words)
        for w in words:
            self.word_set.remove(w)
            if self.search(w):
                ans.append(w)
            self.word_set.add(w)
        return ans
    
    def search(self, w):
        if w in self.word_set:
            return True
        for i in range(1, len(w)):
            if self.search(w[:i]) and self.search(w[i:]):
                return True
        return False

test = Solution()
print test.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])

