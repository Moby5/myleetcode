#!/usr/bin/env python
# coding=utf-8
"""
172. Factorial Trailing Zeroes
题目描述：
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in polynomial time complexity.

题目大意：
给定一个整数n，返回n!（n的阶乘）数字中的后缀0的个数。

注意：你的解法应该满足多项式时间复杂度。

解题思路：
参考博文：http://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/

朴素解法：
首先求出n!，然后计算末尾0的个数。（重复÷10，直到余数非0）

该解法在输入的数字稍大时就会导致阶乘得数溢出，不足取。

O（logn）解法：
一个更聪明的解法是：考虑n!的质数因子。后缀0总是由质因子2和质因子5相乘得来的。如果我们可以计数2和5的个数，问题就解决了。考虑下面的例子：

n = 5: 5!的质因子中 (2 * 2 * 2 * 3 * 5)包含一个5和三个2。因而后缀0的个数是1。

n = 11: 11!的质因子中(2^8 * 3^4 * 5^2 * 7)包含两个5和三个2。于是后缀0的个数就是2。

我们很容易观察到质因子中2的个数总是大于等于5的个数。因此只要计数5的个数就可以了。
那么怎样计算n!的质因子中所有5的个数呢？一个简单的方法是计算floor(n/5)。例如，7!有一个5，10!有两个5。
除此之外，还有一件事情要考虑。诸如25，125之类的数字有不止一个5。例如，如果我们考虑28!，我们得到一个额外的5，并且0的总数变成了6。
处理这个问题也很简单，首先对n÷5，移除所有的单个5，然后÷25，移除额外的5，以此类推。下面是归纳出的计算后缀0的公式。

n!后缀0的个数 = n!质因子中5的个数
              = floor(n/5) + floor(n/25) + floor(n/125) + ....
   
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 5
        ans = 0
        while (n >= x):
            ans += n / x
            x *= 5
        return ans

if __name__ == '__main__':
    solution = Solution()
    query = [5, 11, 7, 10, 25, 125, 28]
    for n in query:
        print n, solution.trailingZeroes(n)
