#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/10/08/leetcode-binary-number-with-alternating-bits/

693. Binary Number with Alternating Bits

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.

题目大意：
给定正整数，判断其二进制是否01交替。
"""

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not bin(n ^ (n >> 1))[2:].count('0')
    
    def hasAlternatingBits_ref1(self, n):  # 解法I 进制转换
        n = bin(n)
        return all (n[x] != n[x + 1] for x in range(len(n) - 1))    
    
    def hasAlternatingBits_ref2(self, n):  # 解法II 位运算
        last = n & 1
        n >>= 1
        while n:
            bit = n & 1
            if bit == last: return False
            last = bit
            n >>= 1
        return True   
    
    def hasAlternatingBits_ref3(self, n):  # Divide By Two  https://leetcode.com/problems/binary-number-with-alternating-bits/solution/
        n, cur = divmod(n, 2)
        while n:
            if cur == n % 2: return False
            n, cur = divmod(n, 2)
        return True    

solution = Solution()
nums = [5, 7, 11, 10, 4]  # T, F, F, T, F
for n in nums:
    print solution.hasAlternatingBits(n)
