#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/10/30/leetcode-arranging-coins/

441. Arranging Coins

You have a total of n coins that you want to form in a staircase shape, 
where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

题目大意：
你有n枚硬币，想要组成一个阶梯形状，其中第k行放置k枚硬币。

给定n，计算可以形成的满阶梯的最大行数。

n是非负整数，并且在32位带符号整数范围之内。

解题思路：
"""

class Solution(object):    
    # 直接枚举
    def arrangeCoins_v0(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        ans = 0
        while(n > ans):
            ans +=1 
            n -= ans
        return ans
    
    """
    解法I 解一元二次方程（初等数学）：
    x ^ 2 + x = 2 * n
    解得：
    x = sqrt(2 * n + 1/4) - 1/2    
    """
    def arrangeCoins_v1(self, n):
        return int(-0.5 + (0.25 + 2 * n) ** 0.5)
        # return int(math.sqrt(2 * n + 0.25) - 0.5)
    
    """
    解法II 二分枚举答案（Binary Search）：
    等差数列前m项和:m * (m + 1) / 2
    在上下界l, r = [0, n]范围内二分枚举答案    
    """
    def arrangeCoins_v2(self, n):
        l, r = 0, n
        while l <= r:
            m = (l + r) / 2
            if m * (m + 1) / 2 > n:
                r = m - 1
            else:
                l = m + 1        
        return r
    
    """
    二分查找的另一种等价实现形式如下
    """
    def arrangeCoins(self, n):
        l, r = 0, n + 1
        while l < r:
            m = (l + r) / 2
            if m * (m + 1) / 2 > n:
                r = m
            else:
                l = m + 1
        return l - 1       
    
test = Solution()    
print test.arrangeCoins(5)
print test.arrangeCoins(8)
        
