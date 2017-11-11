#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/07/13/leetcode-guess-number-higher-or-lower/

374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.

题目大意：
我们来玩猜数字游戏。游戏规则如下：

我挑选一个1到n之间的数字。你来猜我选的是哪个数字。

每一次你猜错，我都会告诉你数字高了还是低了。

你可以调用一个预定义的API guess(int num)，返回3种结果 (-1, 1, 或 0)：

-1 : 我的数字更低
 1 : 我的数字更高
 0 : 恭喜你！猜对了！
测试用例如题目描述。

解题思路：
二分查找（Binary Search）
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
#     pick = 6
#     if pick == num:
#         return 0
#     elif pick > num:
#         return 1
#     else:
#         return -1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid = (low + high)>> 1  # (low + high) / 2
            trial = guess(mid)
            if trial == 0: 
                return mid
            elif trial == 1:
                low = mid + 1                
            else:
                high = mid - 1                          

solution = Solution()
print solution.guessNumber(10)  # 6
