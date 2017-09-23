#!/usr/bin/env python
# coding=utf-8

"""
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

题目大意：
编写一个算法判断某个数字是否是“快乐数”。

快乐数的定义过程如下：从任意一个正整数开始，将原数替换为其每一位的平方和，
重复此过程直到数字=1（此时其值将不再变化），
或者进入一个不包含1的无限循环。那些以1为过程终止的数字即为“快乐数”。

例如：19是一个快乐数，演算过程见题目描述。

解题思路：
模拟题，循环过程中用set记录每次得到的平方和

当出现非1的重复平方和时，返回False

否则，返回True


"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sum_of_squares_of_digits(num):
            ans = 0
            a = num
            while a > 0:
                ans += (a % 10) ** 2
                a = a / 10
            return ans

        num = n
        num_set = set()
        while num != 1 and num not in num_set:
            num_set.add(num)
            num = sum_of_squares_of_digits(num)
            # print num
        return num == 1
                
    def isHappy_v1(self, n):
        numSet = set()
        while n != 1 and n not in numSet:
            numSet.add(n)
            sum = 0
            while n:
                digit = n % 10
                sum += digit * digit
                n /= 10
            n = sum
        return n == 1                
            
        
test = Solution()        
print test.isHappy(19)
print test.isHappy(2)

