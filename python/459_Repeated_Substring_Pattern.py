#!/usr/bin/env python
# coding=utf-8

"""
459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it 
and appending multiple copies of the substring together. 
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

题目大意：
给定一个非空字符串，判断它是否可以通过自身的子串重复若干次构成。你可以假设字符串只包含小写英文字母，并且长度不会超过10000

解题思路：

解法I KMP算法
时间复杂度 O(n)
记字符串长度为size
利用KMP算法求next数组，记next数组的最后一个元素为p
若p > 0 并且 size % (size - p) == 0，返回True
next数组具有如下性质：
str[ 0 : next[i] ] == str[ i + 1 - next[i] : i + 1 ]
例如：
a, b, c, d, a, b, c, a, b, c, d, a, b, c, d, c
0, 0, 0, 0, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 4, 0

解法II 蛮力法（Brute Force）
时间复杂度 O(k * n)，其中n是字符串长度，k是n的约数个数
若字符串可以由其子串重复若干次构成，则子串的起点一定从原串的下标0开始
并且子串的长度一定是原串长度的约数
整数约数的个数可以通过统计其质因子的幂得到，而输入规模10000以内整数的约数个数很少
因此通过蛮力法，枚举子串长度即可
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        total_size = len(s)
        if total_size <= 1: return False
        subs = s[0]
        for ch in s[1:]:
            if ch == subs[0] and len(s) % len(subs) == 0: 
                if subs * (len(s) / len(subs)) == s:
                    return True
            subs += ch
        return False    
    
    def repeatedSubstringPattern_v1(self, str):  # 解法I KMP算法
        """
        :type str: str
        :rtype: bool
        """
        size = len(str)
        next = [0] * size
        for i in range(1, size):
            k = next[i - 1]
            while str[i] != str[k] and k:
                k = next[k - 1]
            if str[i] == str[k]:
                next[i] = k + 1
        p = next[-1]
        return p > 0 and size % (size - p) == 0    
    
    def repeatedSubstringPattern_v2(self, str):  # 解法II 蛮力法（Brute Force）
        """
        :type str: str
        :rtype: bool
        """
        size = len(str)
        for x in range(1, size / 2 + 1):
            if size % x:
                continue
            if str[:x] * (size / x) == str:
                return True
        return False    
            
                
test = Solution()
ss = ['abab', 'aba', 'abcabcabcabc', 'abaababaab']
for s in ss:
    print test.repeatedSubstringPattern(s)
    print 
