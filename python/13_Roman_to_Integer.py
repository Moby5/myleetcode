#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-23

"""
https://leetcode.com/problems/roman-to-integer/description/

13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol2num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        ans, idx, size = 0, 0, len(s)
        while idx < size:
            if idx < size - 1 and s[idx: idx + 2] in symbol2num:
                sym = s[idx: idx + 2]
                idx += 2
            else:
                sym = s[idx]
                idx += 1
            ans += symbol2num[sym]
        return ans
        
    def romanToInt_v1(self, s):
        symbol2num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "a": 4, "b": 9, "c": 40, "d": 90, "e": 400, "f": 900}
        sym2subtraction = {"IV": "a", "IX": "b", "XL": "c", "XC": "d", "CD": "e", "CM": "f"}
        for k, v in sym2subtraction.items():
            s = s.replace(k, v)
        return sum([symbol2num[k] for k in s])
        
    def romanToInt_v2(self, s):
        symbol2num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans, idx, size = 0, 0, len(s)
        for idx, value in enumerate(s):
            if idx < size - 1 and symbol2num[s[idx]] < symbol2num[s[idx + 1]]:
                ans -= symbol2num[s[idx]]
            else:
                ans += symbol2num[s[idx]]
        return ans
        

solutio = Solution()    
ss = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
for s in ss:
    print(s, solutio.romanToInt(s))


"""
https://leetcode.com/problems/roman-to-integer/discuss/152501/My-python-solutionb
    def romanToInt(self, x): 
        foo = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000, "a":4,"b":9,"c":40,"d":90,"e":400,"f":900}
        x = x.replace("IV","a")
        x = x.replace("IX","b")
        x = x.replace("XL","c")
        x = x.replace("XC","d")
        x = x.replace("CD","e")
        x = x.replace("CM","f")
        value= 0
        for i in range(len(x)):
            value += foo[x[i]]
        return value
        
https://leetcode.com/problems/roman-to-integer/discuss/6537/My-Straightforward-Python-Solution        
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]        
"""
