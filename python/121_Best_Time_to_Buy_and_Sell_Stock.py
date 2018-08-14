#!/usr/bin/env python
# coding=utf-8
# Date: 2018-08-14

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
        
    def maxProfit_v1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_price, max_profit = prices[0], 0  # initialize
        for pidx, price in enumerate(prices[1:]):
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
        
    def maxProfit_v0(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return max([max(prices[nidx+1:]) - n for nidx, n in enumerate(prices[:-1])] + [0])   # Time Limit Exceeded


solution = Solution()
for prices in [[7,1,5,3,6,4], [7,6,4,3,1]]:
    print(prices, solution.maxProfit(prices))
        
