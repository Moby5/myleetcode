#!/usr/bin/env python
# coding=utf-8
# Date: 2018-10-15

"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

17_Letter_Combinations_of_a_Phone_Number.py

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution(object):
    def letterCombinations(self, digits):  # 24 ms
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        vmap = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        strs = [vmap[int(d)] for d in digits]
        res = [""]
        for s in strs:
            res = [x+y for x in res for y in s]
        return res


solution = Solution()
digits = "23"
expected_output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
output = solution.letterCombinations(digits)
assert set(expected_output) == set(output), output
print("ok")
        
