#!/usr/bin/env python
# coding=utf-8

import argparse
import math

"""
http://bookshadow.com/weblog/2016/01/08/leetcode-power-three/

题目描述：
Given an integer, write a function to determine if it is a power of three.
Could you do it without using any loop / recursion?

题目大意：
给定一个整数，编写函数判断它是否是3的幂。
进一步思考：
你可以不用循环/递归解出本题吗？

解题思路：
解法1：求对数，然后乘方，判断得数是否相等
解法2：递归
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int 
        :rtype: bool
        """
        return n>0 and 3 ** round(math.log(n, 3))==n
    
    def isPowerOfThree2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        if n==0 or n%3>0:
            return False

        return self.isPowerOfThree(n/3)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='tell if a number is a power of 3')
    parser.add_argument('--num', type=int, help='number to judge')
    args = parser.parse_args()
    print args.num
    test = Solution()
    print test.isPowerOfThree(args.num)
    print test.isPowerOfThree2(args.num)
