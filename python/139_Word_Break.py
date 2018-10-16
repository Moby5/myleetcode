#!/usr/bin/env python
# coding=utf-8
# Date: 2018-10-16

"""
https://leetcode.com/problems/word-break/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

class Solution(object): 
    def wordBreak(self, s, wordDict):  # 36 ms
        """
        另附一段简练的代码，参考LeetCode Discuss
        https://leetcode.com/discuss/41411/4-lines-in-python
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        return ok[-1]

    def wordBreak_v0(self, s, wordDict):  # 36 ms
        """
        BFS（广度优先搜索）：将当前单词拆分为前后两半，若前缀可以在字典dict中找到，则将后缀加入队列。
        http://bookshadow.com/weblog/2015/07/17/leetcode-word-break/
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        queue = [s]
        visited = set([s])
        while queue:
            front = queue.pop(0)
            if front in wordDict:
                return True
            prefix = ""
            for c in front:
                prefix += c
                suffix = front[len(prefix):]
                if prefix in wordDict and suffix not in visited:
                    queue.append(suffix)
                    visited.add(suffix)
        return False


solution = Solution()

s, wordDict, expected_output = "leetcode", ["leet", "code"], True
output = solution.wordBreak(s, wordDict)
assert expected_output == output, output

s, wordDict, expected_output = "applepenapple", ["apple", "pen"], True
output = solution.wordBreak(s, wordDict)
assert expected_output == output, output

s, wordDict, expected_output = "catsandog", ["cats", "dog", "sand", "and", "cat"], False
output = solution.wordBreak(s, wordDict)
assert expected_output == output, output

print("ok") 

