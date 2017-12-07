#!/usr/bin/env python
# coding=utf-8
"""
http://bookshadow.com/weblog/2017/10/01/leetcode-repeated-string-match/

686. Repeated String Match

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. 
If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; 
and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.

题目大意：
给定字符串A和B，求A至少重复几次，才能包含B。若不存在，返回-1。

解题思路：
蛮力法
"""

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        ans = 1
        lenA = len(A)
        thres = 2 * max(lenA, len(B))
        while ans * lenA <= thres:
            if B in A * ans:
                return ans
            ans += 1
        return -1  
    
    def repeatedStringMatch_ref(self, A, B):
        sa, sb = len(A), len(B)
        x = 1
        while x * sa <= 2 * max(sa, sb):
            if B in A * x: return x
            x += 1
        return -1    
    
    def repeatedStringMatch_ref2(self, A, B):  # Ad-Hoc   https://leetcode.com/problems/repeated-string-match/solution/
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1    
        
solution = Solution()        
print solution.repeatedStringMatch("abcd", "cdabcdab") # 3
print solution.repeatedStringMatch("aa", "a") # 1
print solution.repeatedStringMatch("abababaaba", "aabaaba") # 2
print solution.repeatedStringMatch("a", "aa") # 2
print solution.repeatedStringMatch("a", "aaa") # 3
