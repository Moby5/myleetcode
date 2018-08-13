#!/usr/bin/env python
# coding=utf-8
# Date: 2018-08-13

"""
https://leetcode.com/problems/valid-parentheses/description/

20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lefts, rights = {"(", "[", "{"}, {")", "]", "}"}
        right2left = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in lefts:
                stack.append(ch)
            elif ch in rights:
                if stack and stack[-1] == right2left[ch]:
                    stack.pop()
                else:
                    return False
        return not stack

    def isValid_v0(self, s):
        """
        :type s: str
        :rtype: bool
        """
        right2left = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in right2left:
                if stack and stack[-1] == right2left[ch]:
                    stack.pop()
                else:
                    return False            
            else:
                stack.append(ch)
        return not stack        
        

solution = Solution()
for s in ["", "()", "()[]{}", "(]", "([)]", "{[]}"]:
    print(s, solution.isValid(s))

        
