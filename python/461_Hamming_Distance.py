#!/usr/bin/env python
# coding=utf-8
# 461_hamming_distance.py

"""
http://bookshadow.com/weblog/2016/12/18/leetcode-hamming-distance/

LeetCode 461. Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 231.
"""

class Solution(object):
    def hamming_distance(self, x, y):
        """
        两个整数的汉明距离是指其二进制不相等的位的个数。
        给定两个整数x和y，计算汉明距离。
        :type x: int
        :type y: int
        :rtype: int
        """

        return bin(x ^ y).count('1')


if __name__ == '__main__':
    solution = Solution()
    print solution.hamming_distance(1, 4)
    

'''
def bin(number): # real signature unknown; restored from __doc__
    """
    bin(number) -> string
    
    Return the binary representation of an integer or long integer.
    """
    return ""


def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
    """
    S.count(sub[, start[, end]]) -> int

    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are interpreted
    as in slice notation.
    """
    return 0
'''

