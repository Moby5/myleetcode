#!/usr/bin/env python
# coding=utf-8
# 566_reshape_the_matrix.py

"""
http://bookshadow.com/weblog/2017/07/09/leetcode-solve-the-equation/

LeetCode 640. Solve the Equation

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:

Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:

    Input: "x=x"
    Output: "Infinite solutions"
    Example 3:

        Input: "2x=x"
        Output: "x=0"
        Example 4:

            Input: "2x+3x-6x=x+2"
            Output: "x=-1"
            Example 5:

                Input: "x=x+2"
                Output: "No solution"
                题目大意：
                给定一元一次方程，求x的值

                解题思路：
                字符串处理

                用'='将等式分为左右两半

                分别求左右两侧x的系数和常数值，记为lx, lc, rx, rc

                令x, c = lx - rx, rc - lc

                若x != 0，则x = c / x

                否则，若c != 0，说明方程无解

                否则，说明有无数组解
"""


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        lcoef, lconst = self.solve(left)
        rcoef, rconst = self.solve(right)
        coef, const = lcoef - rcoef, rconst - lconst
        if coef: return 'x=%d' % (const / coef)
        elif const: return 'No solution'
        return 'Infinite solutions'

    def solve(self, expr):
        coef = const = 0
        num, sig = '', 1
        for ch in expr + '#':
            if '0' <= ch <= '9':
                num += ch
            elif ch == 'x':
                coef += int(num or '1') * sig
                num, sig = '', 1
            else:
                const += int(num or '0') * sig
                num, sig = '', 1
                if ch == '-': sig = -1
        return coef, const


if __name__ == '__main__':
    solution = Solution()
    equations = ["x+5-3+x=6+x-2", "x=x" ,"2x=x", "2x+3x-6x=x+2", "x=x+2"]
    for e in equations:
        print e, solution.solveEquation(e)
    pass
