#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/10/29/leetcode-1-bit-and-2-bit-characters/

717. 1-bit and 2-bit Characters

We have two special characters. The first character can be represented by one bit 0. 
The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. 
Return whether the last character must be a one-bit character or not. 
The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.

题目大意：
01序列由三种成分构成：10, 11, 0

求序列经过解析后，最后一个成分是否为0

解题思路：
模拟题

https://leetcode.com/problems/1-bit-and-2-bit-characters/solution/
"""

class Solution(object):
    def isOneBitCharacter_v0(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        idx = 0
        size = len(bits)
        while idx < size:
            if idx == size - 1: return True
            if bits[idx] == 0: idx += 1
            else: idx += 2 
        return False
    
    def isOneBitCharacter(self, bits):  # Increment Pointer
        idx = 0
        size = len(bits)
        while idx < size - 1:
            idx += bits[idx] + 1
        return idx == size - 1
    
    
    def isOneBitCharacter_ref2(self, bits):  #Greedy
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0        
            
        
solution = Solution()        
print solution.isOneBitCharacter([1,0,0])     # True
print solution.isOneBitCharacter([1,1,1,0])   # False
