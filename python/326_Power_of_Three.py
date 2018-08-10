#!/usr/bin/env python
# coding=utf-8
# Date: 2018-08-10

"""
https://leetcode.com/problems/power-of-three/description/

326. Power of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
"""

import math

class Solution(object):
    def isPowerOfThree(self, n):  # Loop Iteration
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1
        
    def isPowerOfThree_v0(self, n):  # Mathematics
        """
        :type n: int
        :rtype: bool
        """
        # return n > 0 and str(math.log(n, 3)).endswith(".0")  # Accepted
        # return n > 0 and math.log(n, 3) % 1 == 0  # Wrong Answer  # 243  # 存在精度问题
        return n > 0 and (math.log10(n) / math.log10(3)) % 1 == 0   # Accepted

solution = Solution()
for n in [-1, 0, 3, 9, 27, 45]:
    print(n, solution.isPowerOfThree(n))
        

"""
https://leetcode.com/problems/power-of-three/solution/

Approach #1 Loop Iteration [Accepted]
public class Solution {
    public boolean isPowerOfThree(int n) {
        if (n < 1) {
            return false;
        }

        while (n % 3 == 0) {
            n /= 3;
        }

        return n == 1;
    }
}

Approach #2 Base Conversion [Accepted]
public class Solution {
    public boolean isPowerOfThree(int n) {
        return Integer.toString(n, 3).matches("^10*$");
    }
}

Approach #3 Mathematics [Accepted]
public class Solution {
    public boolean isPowerOfThree(int n) {
        return (Math.log10(n) / Math.log10(3)) % 1 == 0;
    }
}

Approach #4 Integer Limitations [Accepted]
public class Solution {
    public boolean isPowerOfThree(int n) {
        return n > 0 && 1162261467 % n == 0;
    }
}
"""        
