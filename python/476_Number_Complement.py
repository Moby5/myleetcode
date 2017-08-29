#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/01/08/leetcode-number-complement/

476. Number Complement

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

题目大意：
给定一个正整数，输出其补数。补充策略就是按二进制位反转。

注意：

给定正数确保是32位带符号整数。
可以假设整数的二进制表示不包含前导0。
"""

import math
class Solution(object):
    def findComplement(self, num):  # 按位取反并累加
        """
        :type num: int
        :rtype: int
        """
        nbin = bin(num)[2:] # 十进制转二进制
        cbin = ''.join([str(int(bit) ^ 1) for bit in nbin]) #逐位取反
        return int(cbin, 2) # 二进制转十进制
        # return int(''.join([str(int(bit) ^ 1) for bit in bin(num)[2:]]), 2)
        # return int(''.join(str(1 - int(bit)) for bit in bin(num)[2:]), 2)
        
    def findComplement_v2(self, num):  # 位运算（异或）
        """
        :type num: int
        :rtype: int
        """     
        mask = (1 << 1 + int(math.log(num, 2))) - 1
        return mask ^ num

test = Solution()
nums = [5, 1]
for num in nums:
    print 'The complement number of %d is %d' % (num, test.findComplement_v2(num))
