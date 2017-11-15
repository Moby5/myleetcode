#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/06/30/leetcode-sum-of-two-integers/

371. Sum of Two Integers

Calculate the sum of two integers a and b, 
but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

题目大意：
不使用加减法，计算两个整数a和b的和。

解题思路：

解法I 位运算（Bit Manipulation）异或 + 移位
参考：http://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/        
Java代码：
public class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int c = a ^ b;
            b = (a & b) << 1;
            a = c;
        }
        return a;
    }
}    

解法II 位运算（Bit Manipulation) 模拟加法
Java代码：
public class Solution {
    public int getSum(int a, int b) {
        int r = 0, c = 0, p = 1;
        while ((a | b | c) != 0) {
            if (((a ^ b ^ c) & 1) != 0)
                r |= p;
            p <<= 1;
            c = (a & b | b & c | a & c) & 1;
            a >>>= 1;
            b >>>= 1;
        }
        return r;
    }
}

由于Python没有无符号右移操作，并且当左移操作的结果超过最大整数范围时，会自动将int类型转换为long类型，因此需要对上述两种代码进行调整。
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """          
        MAX_INT = 0x7FFFFFFF
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a & MAX_INT) ^ MAX_INT)           

    
    def getSum_ref2(self, a, b):
        MAX_INT = 0x7FFFFFFF
        MASK = 0x100000000
        r, c, p = 0, 0, 1
        while a | b | c:
            if (a ^ b ^ c) & 1: r = (r | p) % MASK
            p <<= 1
            c = (a & b | b & c | a & c) & 1
            a = (a >> 1) % MASK
            b = (b >> 1) % MASK
        return r if r <= MAX_INT else ~((r & MAX_INT) ^ MAX_INT) 
    # 上述代码中的 ~((r & MAX_INT) ^ MAX_INT) 可以简化为 (~0 << 31) | r ，感谢 @大王驮我去巡山 补充。
            
               
solution = Solution()
print solution.getSum(1, 2)
print solution.getSum(3, 5) 
print solution.getSum(11, 22)
