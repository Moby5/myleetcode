#!/usr/bin/env python
# coding=utf-8
# Date: 2018-08-21

"""
https://leetcode.com/problems/reverse-integer/description/

7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = int(str(x)[::-1]) if x >= 0 else int("-" + str(x)[1:][::-1])
        return 0 if ans < -2**31 or ans > (2**31 - 1) else ans

solution = Solution()
for x in [123, -123, 120]:
    print(x, solution.reverse(x))

        
