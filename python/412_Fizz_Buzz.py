#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/10/09/leetcode-fizz-buzz/

412. Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

题目大意：
编写程序输出数字1-n的字符串形式。

但是对于3的倍数输出 “Fizz”，5的倍数输出“Buzz”。既是3的倍数，又是5的倍数输出“FizzBuzz”。

解题思路：
模拟题，略	
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 ==0: 
                ans.append('FizzBuzz')
            elif i % 3 ==0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i))
        return ans

    def fizzBuzz_ref(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
        
test = Solution()
print test.fizzBuzz(15)

