#!/usr/bin/env python
# coding=utf-8

"""
# not understood yet

http://bookshadow.com/weblog/2016/09/18/leetcode-nth-digit/

400. Nth Digit

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 2^31).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

题目大意：
给定一个无穷整数序列1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 求序列的第n位数字。

注意：

n是正数并且范围在32位带符号整数之内（n < 2^31）

解题思路：
将整数序列划分为下列区间：

1   1-9
2   10-99
3   100-999
4   1000-9999
5   10000-99999
6   100000-999999
7   1000000-9999999
8   10000000-99999999
9   100000000-99999999
然后分区间求值即可。
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(9):
            # print 'i:', i
            d = 9 * 10 ** i
            # print 'd:', d
            if n <= d * (i + 1): break
            n -= d * (i + 1)
            # print 'n:', n
        n -= 1
        # print 'n:', n
        return int(str(10**i + n / (i + 1))[n % (i + 1)])
        
    def findNthDigit_ref(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(9):
            d = 9 * 10 ** i
            if n <= d * (i + 1): break
            n -= d * (i + 1)
        n -= 1
        return int(str(10**i + n / (i + 1))[n % (i + 1)])
        
       
test = Solution()
nums = [3, 11, 100]
for n in nums:
    print n, test.findNthDigit(n)

