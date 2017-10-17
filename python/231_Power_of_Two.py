#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/07/06/leetcode-power-of-two/

231. Power of Two

Given an integer, write a function to determine if it is a power of two.

题目大意：
给定一个整数，编写函数判断它是否是2的幂。

解题思路：
如果一个整数是2的幂，那么它的二进制形式最高位为1，其余各位为0

等价于：n & (n - 1) = 0，且n > 0
"""

from math import pow, log

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        l, r = 0, n-1
        target = log(n, 2)
        # print 'target:', target, 
        if str(target).split('.')[1] != '0': return False
        target = int(target)
        while(l <= r):
            m = (l + r) / 2
            if m == target: return True
            elif m > target: r = m - 1
            else: l = m + 1
        return False

    def isPowerOfTwo_ref(self, n):
        return n > 0 and n & (n - 1) == 0


test = Solution()
for i in range(10):
    print i, test.isPowerOfTwo(i)

n = 536870912 
print n, test.isPowerOfTwo(n)  # True

