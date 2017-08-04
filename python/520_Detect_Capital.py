#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/02/19/leetcode-detect-capital/

题目描述：
LeetCode 520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital if it has more than one letter, like "Google"
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

题目大意：
判断单词是否为首字母大写、全部大写或者全部小写

注意：输入单词非空并且只包含大写或者小写字母

解题思路：
字符串处理
"""

class Solution(object):
    class detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # return word.isupper() or word.islower() or word[1:].islower()
        return word.isupper() or word.islower() or (len(word) > 1 and word[0].isupper() and word[1:].islower())

