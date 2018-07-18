#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-18

"""
https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

762. Prime Number of Set Bits in Binary Representation

Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
Note:

L, R will be integers L <= R in the range [1, 10^6].
R - L will be at most 10000.
"""

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count("1") in primes for x in xrange(L, R+1))

solution = Solution()    
print solution.countPrimeSetBits(6, 10)
print solution.countPrimeSetBits(10, 15)
        
        
"""
https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/solution/

Intuition and Approach
For each number from L to R, let's find out how many set bits it has. If that number is 2, 3, 5, 7, 11, 13, 17, or 19, then we add one to our count. We only need primes up to 19 because R ≤ 10^​6​​ < 2^​20​.

class Solution(object):
    def countPrimeSetBits(self, L, R):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes
                   for x in xrange(L, R+1))
"""        
        
"""
http://bookshadow.com/weblog/2018/01/14/leetcode-prime-number-of-set-bits-in-binary-representation/

题目大意：
求范围[L, R]的整数中，二进制表示中1的个数为素数的整数个数

解题思路：
埃拉托斯特尼筛法

类似题目：http://bookshadow.com/weblog/2015/04/27/leetcode-count-primes/

class Solution(object):
    def __init__(self):
        MAXN = 100
        self.prime = [1] * (MAXN + 1)
        self.prime[0] = self.prime[1] = 0
        for x in range(2, MAXN + 1):
            if self.prime[x]:
                y = x ** 2
                while y <= MAXN:
                    self.prime[y] = 0
                    y += x
    def countPrimeSetBits(self, L, R):
        ans = 0
        for x in range(L, R + 1):
            ans += self.prime[bin(x).count('1')]
        return ans
"""        
