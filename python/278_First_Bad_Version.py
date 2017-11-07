#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/09/07/leetcode-first-bad-version/

278. First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

题目大意：
你是一名产品经理，正在领导团队开发一个新产品。不幸的是，产品的最新版本没有通过质量检测。由于每一个版本都是基于上一个版本开发的，某一个损坏的版本之后的所有版本全都是坏的。

假设有n个版本[1, 2, ..., n]，你想要找出第一个损坏的版本，它导致所有后面的版本都坏掉了。

给你一个API bool isBadVersion(version)，返回某一个版本是否损坏。实现一个函数找出第一个损坏的版本。你应该最小化调用API的次数。

解题思路：
二分法（Binary Search），详见代码。

Input:
3 versions
1 is the first bad version.

Expected:
1
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >= 1

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """        
        low, high = 1, n
        while(low <= high):
            mid = (low + high) / 2            
            if isBadVersion(mid): high = mid -1
            else: low = mid + 1
        return low   
            
test = Solution()            
print test.firstBadVersion(1)  # 1
print test.firstBadVersion(3)  # 1
 
