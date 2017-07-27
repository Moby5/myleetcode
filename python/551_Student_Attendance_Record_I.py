#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/04/16/leetcode-student-attendance-record-i/

LeetCode 551. Student Attendance Record I

You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:

Input: "PPALLP"
Output: True
Example 2:

Input: "PPALLL"
Output: False
题目大意：
给定一个字符串s，若其中的'A'大于1个，或者出现连续的3个或3个以上'L'，返回False，否则返回True

解题思路：
字符串处理
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') <= 1 and 'LLL' not in s


if __name__ == '__main__':
    test = Solution()
    print test.checkRecord('PPALLP')
    print test.checkRecord('PPALLL')

