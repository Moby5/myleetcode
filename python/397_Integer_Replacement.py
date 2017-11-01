#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/09/11/leetcode-integer-replacement/

LeetCode 397. Integer Replacement

Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1

题目大意：
给定正整数n，你可以做如下操作：

如果n是偶数，将n替换为n/2

如果n是奇数，你可以将n替换为n + 1或者n - 1

求将n替换为1的最小次数


解题思路：

解法I 直接递归求解
由于递归深度较小，因此直接根据题意递归求解即可


解法II 位运算（Bit Manipulation）
参考LeetCode Discuss，链接地址：https://discuss.leetcode.com/topic/58334/a-couple-of-java-solutions-with-explanations/
该解法采用迭代方式求解。
当n为偶数时，下一次迭代n的取值确定为n / 2；
当n为奇数时，下一次迭代n的取值n + 1或者n - 1，由其二进制表示中的最低两位数决定：
若n的最低两位数为01，则令n = n - 1
否则，若n的最低两位数为11，则令n = n + 1
这样处理是为了使n的二进制表式中1的数目尽可能少，从而减少迭代次数
需要注意的是，当n = 3时，不满足上述判定条件，需要单独处理。
"""

class Solution(object):
    def integerReplacement_v0(self, n):
        """
        :type n: int
        :rtype: int
        """        
        if n == 1: 
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n/2)
        else:
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))        
    
    def integerReplacement_ref1(self, n):
        if n == 1: return 0
        if n & 1 == 0: return self.integerReplacement(n / 2) + 1
        return min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1
    
    def integerReplacement(self, n): # ref2 效率最高
        ans = 0
        while n != 1:
            if n & 1 == 0:
                n /= 2
            elif n == 3 or (n >> 1) & 1 == 0:
                n -= 1
            else:
                n += 1
            ans += 1
        return ans       
    
    
test = Solution()
nums = [8, 7]  # 3, 4
for n in nums:
    print n, test.integerReplacement(n)
        
