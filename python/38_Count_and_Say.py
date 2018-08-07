#!/usr/bin/env python
# coding=utf-8
# Date: 2018-08-07

"""
https://leetcode.com/problems/count-and-say/description/

38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """        
        if n == 1:
            return "1"
        last = str(self.countAndSay(n - 1))
        ans = [[1, last[0]]]
        for cidx, ch in enumerate(last[1:]):
            if ch == ans[-1][1]:
                ans[-1][0] += 1
            else:
                ans.append([1, ch])
        return "".join([str(item[0]) + str(item[1]) for item in ans])


solution = Solution()
for n in range(1, 16):
    print(n, solution.countAndSay(n))


"""
https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions


Solution 1 ... using a regular expression

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s
    
    
Solution 2 ... using a regular expression

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(group)) + digit
                    for group, digit in re.findall(r'((.)\2*)', s))
    return s


Solution 3 ... using groupby

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + digit
                    for digit, group in itertools.groupby(s))
    return s
"""

