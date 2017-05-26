#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/05/07/leetcode-distribute-candies/

LeetCode 575. Distribute Candies
Given an integer array with even length, where different numbers in this array represent different kinds of candies.
Each number means one candy of the corresponding kind.
You need to distribute these candies equally in number to brother and sister.
Return the maximum number of kinds of candies the sister could gain.

Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.

Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.

Note:
The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].

题目大意：
给定一组长度为偶数的整数，其中每个数字代表一个糖果的种类标号。
将糖果均分给哥哥和妹妹，返回妹妹可以得到的最大糖果种类数。

注意：
数组长度范围[2, 10,000]，并且为偶数
给定数字范围[-100,000, 100,000]

解题思路：
返回 min( 糖果总数的一半, 糖果种类数 ) 即可
"""


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies) / 2, len(set(candies)))


if __name__ == '__main__':
    solution = Solution()
    print solution.distributeCandies([1,1,2,2,3,3])
    print solution.distributeCandies([1,1,2,3])
