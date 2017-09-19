#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/04/01/leetcode-house-robber/

198. House Robber

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

解题思路：
动态规划（Dynamic Programming）
状态转移方程：
dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])
其中，dp[i]表示打劫到第i间房屋时累计取得的金钱最大值。
时间复杂度O(n)，空间复杂度O(n)
"""  

class Solution(object):     
    def rob(self, nums): # 动态规划（Dynamic Programming） 时间复杂度O(n)，空间复杂度O(n)
        """
        :type nums: List[int]
        :rtype: int
        """    
        size = len(nums)
        if size == 0: return 0
        dp = []
        dp.extend([0, nums[0]])        
        for i in range(1, size):            
            dp.append(max(dp[-1], dp[-2] + nums[i]))        
        return dp[-1]
    
    def rob(self, num):
        size = len(num)
        dp = [0] * (size + 1)
        if size:
            dp[1] = num[0]
        for i in range(2, size + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])
        return dp[size]
    
    def rob_v1(self, nums):  # 上述代码的空间复杂度可以进一步化简为O(1):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd, even = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:  # odd 奇数
                odd = max(even, nums[i] + odd)
            else:
                even = max(odd, nums[i] + even)
        return max(odd, even)  
    
    def rob_v1(self, num):
        size = len(num)
        dp = [0] * (size + 1)
        if size:
            dp[1] = num[0]
        for i in range(2, size + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])
        return dp[size]       

test = Solution()
print test.rob([1, 2, 3, 4, 5])

