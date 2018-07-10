#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-10

"""
https://leetcode.com/problems/shortest-distance-to-a-character/description/

821. Shortest Distance to a Character

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""

from collections import defaultdict

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        char2idxes = defaultdict(list)
        for cidx, ch in enumerate(S):
            char2idxes[ch].append(cidx)
        return [min([abs(cidx - c) for c in char2idxes[C]]) for cidx, ch in enumerate(S)]
         
       
solution = Solution()
print solution.shortestToChar("loveleetcode", "e")


"""
http://bookshadow.com/weblog/2018/04/22/leetcode-shortest-distance-to-a-character/

题目大意：
给定字符串S和字符C，求S中的每个字符距离其最近的C的距离

解题思路：
正反两次遍历S

用变量lastC记录C最后一次出现的下标

class Solution(object):
    def shortestToChar(self, S, C):
        INF = 0x7FFFFFFF
        N = len(S)
        ans = [INF] * N
        lastC = -INF
        for i in range(N):
            if S[i] == C: lastC = i
            ans[i] = min(ans[i], i - lastC)

        lastC = INF
        for i in range(N - 1, -1, -1):
            if S[i] == C: lastC = i
            ans[i] = min(ans[i], lastC - i)
        return ans
"""
