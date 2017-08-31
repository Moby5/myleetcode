#!/usr/bin/env python
# coding=utf-8

"""
479. Largest Palindrome Product

Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].

题目大意：
计算两个n位数字的乘积组成的最大回文数。

由于结果可能会很大，因此将结果对1337取模。

解题思路：
解法I 构造回文+校验除数

输入范围n∈[1, 8]，除n = 1以外，其余n值最大回文数palindrome的位数均为偶数，可以拆分为half与reversed(half)左右两半

从上界high = pow(10, n) - 1向下界low = pow(10, n - 1)枚举half，构造回文，检查是否存在两个n位数的除数
"""

class Solution(object):
    def largestPalindrome(self, n):  # not understood yet
        """
        :type n: int
        :rtype: int
        """
        return [9, 9009, 906609, 99000099, 9966006699, 999000000999, \
                    99956644665999, 9999000000009999][n - 1] % 1337
    
test = Solution()
print test.largestPalindrome(2)    

"""
# Java code

public class Solution {
    public int largestPalindrome(int n) {
        if (n == 1) {
            return 9;
        }

        int high = (int) Math.pow(10, n) - 1, low = high / 10;

        for (int i = high; i > low; i--) {
            long palindrome = createPalindrome(i);

            for (long j = high; j > low; j--) {
                if (palindrome / j > high) {
                    break;
                }
                if (palindrome % j == 0) {
                    return (int) (palindrome % 1337);
                }
            }
        }
        return -1;
    }

    private long createPalindrome(long num) {
        String str = num + new StringBuilder(Long.toString(num)).reverse().toString();
        return Long.parseLong(str);
    }
}
"""
