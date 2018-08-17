#!/usr/bin/env python
# coding=utf-8
# Date: 2018-08-17

"""
https://leetcode.com/problems/longest-common-prefix/description/

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        for chs in zip(*strs):
            chs_set = set(chs)
            if len(chs_set) == 1:
                ans += chs_set.pop()
            else:
                return ans
        return ans
        
    def longestCommonPrefix_v0(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        ans = ""
        min_len = min([len(s) for s in strs])
        for cidx in range(min_len):
            if len({s[cidx] for s in strs}) == 1:
                ans += strs[0][cidx]
            else:
                break
        return ans

solution = Solution()
for strs in [["flower","flow","flight"], ["dog","racecar","car"], ["aca","cba"], []]:
    print(strs, solution.longestCommonPrefix(strs))
    

"""
https://leetcode.com/problems/longest-common-prefix/discuss/159148/A-simple-Python-approach-with-standard-library

    def longestCommonPrefix(self, strs):        
        if not strs:
            return ''
        from itertools import takewhile
        max_pre_len = len(list(takewhile(lambda x: len(set(x))==1, zip(*strs))))
        return strs[0][:max_pre_len]
"""

