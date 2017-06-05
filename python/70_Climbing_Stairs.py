#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/08/23/leetcode-climbing-stairs/

[LeetCode] 70. Climbing Stairs
题目描述：
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

题目大意：
你正在爬楼梯。爬到顶部需要n步。
每一次你爬1步或者2步。爬到顶部有多少种不同的方式？

解题思路：
问题的本质是求斐波那契数列（Fibonacci Sequence）
递推式为：dp[x] = dp[x - 1] + dp[x - 2]
"""


class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for x in range(2, n + 1):
            dp[x] = dp[x - 1] + dp[x - 2]
        return dp[n]


class Solution2:  # 空间复杂度O(1)：
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        a = b = 1
        for x in range(2, n + 1):
            a, b = b, a + b
        return b


'''
使用斐波那契数列的通项公式求解：
an = [ (Phi)^n - (phi)^n ]/Sqrt[5].
其中，Phi=(1+Sqrt[5])/2，phi=(1-Sqrt[5])/2'''
import math
class Solution3:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        sqrt5 = math.sqrt(5)
        Phi = (1 + sqrt5) / 2
        phi = (1 - sqrt5) / 2
        return int((Phi ** (n + 1) - phi ** (n + 1)) / sqrt5)

# 其它参考解: https://leetcode.com/articles/climbing-stairs/

if __name__ == '__main__':
    solution = Solution3()
    print solution.climbStairs(5)
