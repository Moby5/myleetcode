#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/02/05/leetcode-keyboard-row/

题目描述：
LeetCode 500. Keyboard Row

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

American keyboard

Example 1:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
题目大意：
给定一组单词，返回可以用美式键盘中的某一行字母键入的所有单词。

注意：

键盘中的字符可以使用多次
可以假设输入只包含小写或者大写字母
解题思路：
集合运算

判断输入单词的字母集合是否为键盘某一行字母集合的子集
"""

import numpy as np
from collections import defaultdict

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rs = map(set, ['qwertyuiop','asdfghjkl','zxcvbnm'])
        ans = []
        for word in words:
            wset = set(word.lower())   
            if any(wset <= rset for rset in rs):
                ans.append(word)
        return ans
    
    def findWords_v2(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """        
        w2row = {w: 1 for w in 'qwertyuiop'}           
        for w in 'asdfghjkl': w2row[w] = 2
        for w in 'zxcvbnm': w2row[w] = 3        
        ans = []            
        for i, word in enumerate(words):
            if len(np.unique([w2row[w] for w in word.lower()])) <= 1:
                ans.append(word)
        return ans
            
    
test = Solution()
print test.findWords(["Hello", "Alaska", "Dad", "Peace"])
