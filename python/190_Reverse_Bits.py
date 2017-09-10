#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/03/08/leetcode-reverse-bits/

190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.
For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

题目大意：
按位反转一个给定的32位无符号整数。

例如，输入整数43261596（二进制形式为：00000010100101000001111010011100），返回964176192（转换为二进制为00111001011110000010100101000000）。

进一步思考：
如果函数需要被调用很多次，怎样优化？

解题思路：
位操作（bit manipulation）


优化方案：
参考：https://oj.leetcode.com/discuss/27338/8ms-c-code-some-ideas-about-optimization-spoiler

以4位为单位执行反转，将0x0至0xF的反转结果预存在一个长度为16的数组中，反转时直接查询即可。
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        nbit = bin(n)[2:]
        nbit = '0' * (32 - len(nbit)) + nbit 
        return int(nbit[::-1], 2)
    
    def reverseBits_v2(self, n):  # 朴素解法 (not understood yet)
        ans = 0
        for i in range(32):
            ans <<= 1            
            ans |= n & 1
            n >>= 1
        return ans    

test = Solution()
print test.reverseBits(43261596) 
print test.reverseBits(964176192)

