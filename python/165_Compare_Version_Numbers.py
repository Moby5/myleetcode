#!/usr/bin/env python
# coding=utf-8

"""
https://leetcode.com/problems/compare-version-numbers/description/

165. Compare Version Numbers

题目描述：
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

题目大意：
比较两个版本号version1和version2。

如果version1 > version2返回1，如果version1 < version2返回-1，否则返回0.

你可以假设版本号字符串均非空并且只包含数字和点号。

点号不代表数字的小数点，用来分割数字序列。

例如，2.5不是“2又2分之1”或者“差一半到版本3”，它是第二级别的第5版本，第一级别的第2版本。

下面是版本号顺序的实例：

0.1 < 1.1 < 1.2 < 13.37
"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """    
        v1, v2 = version1.split('.'), version2.split('.')
        max_len = max(len(v1), len(v2))
        for i in range(max_len):
            num1 = 0 if i >= len(v1) else int(v1[i])
            num2 = 0 if i >= len(v2) else int(v2[i])
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0    

    def compareVersion_v2(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """       
        v1Arr = version1.split(".")
        v2Arr = version2.split(".")
        len1 = len(v1Arr)
        len2 = len(v2Arr)
        lenMax = max(len1, len2)
        for x in range(lenMax):
            v1Token = 0
            if x < len1:
                v1Token = int(v1Arr[x])
            v2Token = 0
            if x < len2:
                v2Token = int(v2Arr[x])
            if v1Token < v2Token:
                return -1
            if v1Token > v2Token:
                return 1
        return 0    
        
test = Solution()
print test.compareVersion('1.0', '1')  # 0
print test.compareVersion('1', '1.1')  # -1
print test.compareVersion('1.2', '1.10')  # -1
print test.compareVersion('01', '1') # 0
print test.compareVersion('1', '01') # 0
print test.compareVersion('0.1', '0.0.1') # 1
print test.compareVersion('4.08', '4.08.01') # -1
