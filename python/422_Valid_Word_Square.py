#!/usr/bin/env python
# coding=utf-8

"""
LeetCode 422. Valid Word Square

Given a sequence of words, check whether it forms a valid word square.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

Note:

The number of words given is at least 1 and does not exceed 500.
Word length will be at least 1 and does not exceed 500.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".
Therefore, it is a valid word square.

Example 2:

Input:
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".
Therefore, it is a valid word square.

Example 3:

Input:
[
  "ball",
  "area",
  "read",
  "lady"
]

Output:
false

Explanation:
The third row reads "read" while the third column reads "lead".

Therefore, it is NOT a valid word square.

题目大意：
给一组单词，判断它们是不是有效的“四方连词”

一组单词如果其第k行和第k列组成的单词相同，其中0 ≤ k < max(numRows, numColumns)，则称其为一个“四方连词”。

注意：

单词个数在[1, 500]之间
单词长度在[1, 500]之间
每个单词只包含小写字母a-z
解题思路：
O(m * n)循环遍历即可，m为单词个数，n为单词长度。

需要注意的是每一行单词的长度可能不同。
"""

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        size = len(words)
        for i in range(len(words)):
            row = words[i]
            for j in range(i+1, len(row)):
                if j >= size: return False
                if words[j][i] != words[i][j]: return False
        return True
        
    def validWordSquare_v1(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        m = len(words)
        n = len(words[0]) if m else 0
        if m != n:
            return False
        for x in range(m):
            n = len(words[x])
            c = 0
            for y in range(m):
                if len(words[y]) < x + 1:
                    break
                c += 1
            if c != n:
                return False
            for y in range(n):
                if words[x][y] != words[y][x]:
                    return False
        return True        

test = Solution()
print test.validWordSquare(["abcd", "bnrt", "crmy", "dtye"])
print test.validWordSquare(["abcd", "bnrt", "crm", "dt"])
print test.validWordSquare(["ball", "area", "read", "lady"])
        
