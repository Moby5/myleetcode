#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/03/10/leetcode-number-1-bits/

191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of ’1' bits it has 
(also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, 
so the function should return 3.

题目大意：
编写函数接收一个无符号整数，返回其二进制形式中包含的1的个数（也叫做汉明权重）

例如，32位整数'11'的二进制表示为：00000000000000000000000000001011，因此函数应当返回3

解题思路：
位操作（bit manipulation）
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n)[2:].count('1')
    
    def hammingWeight_v1(self, n):
        ans = 0
        while n:
            ans += n & 1            
            n >>= 1
        return ans   
    
    def hammingWeight_v2(self, n):
        ans = 0
        while n:            
            n &= n - 1
            ans += 1
        return ans    
        
test = Solution()
print test.hammingWeight(11)
