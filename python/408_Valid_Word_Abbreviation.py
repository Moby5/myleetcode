#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/10/02/leetcode-valid-word-abbreviation/

LeetCode 408. Valid Word Abbreviation

Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:

Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:

Given s = "apple", abbr = "a2e":

Return false.

题目大意：
给定一个非空字符串s以及一个单词缩写abbr，返回字符串是否与单词缩写相匹配。

一个诸如"word"的字符串只包含如下有效的缩写：

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

请注意只有上面的缩写是"word"的有效缩写。其他任何字符串都不是"word"的有效缩写。其他任何字符串都不是

注意：

假设s只包含小写字母，abbr只包含小写字母和数字。

解题思路：
模拟题，遍历word和abbr即可。
"""

class Solution(object):           
    def validWordAbbreviation(self, word, abbr):
        size = len(word)
        loc, cnt = 0, 0
        for ch in abbr:
            if ch.isdigit():
                if ch == '0':
                    return False
                cnt = cnt * 10 + int(ch)
            else:
                loc += cnt
                cnt = 0
                if loc > size or word[loc] != ch:
                    return False
                loc += 1
        return True
            
    def validWordAbbreviation_ref(self, word, abbr):
        size = len(word)
        cnt = loc = 0
        for w in abbr:            
            if w.isdigit():
                if w == '0' and cnt == 0:
                    return False
                cnt = cnt * 10 + int(w)
            else:
                loc += cnt
                cnt = 0
                if loc >= size or word[loc] != w:
                    return False
                loc += 1
        return loc + cnt == size            
                    
        
test = Solution()
print '\n', test.validWordAbbreviation('internationalization', 'i12iz4n')  # True
print '\n', test.validWordAbbreviation('apple', 'a2e')  # False
print '\n', test.validWordAbbreviation('apple', '0apple')  # False

word_abbrs = ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
for abbr in word_abbrs:
    print '\n', test.validWordAbbreviation('word', abbr)  # True
