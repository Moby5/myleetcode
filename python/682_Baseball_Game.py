#!/usr/bin/env python
# coding=utf-8
# Date: 2018-01-08


"""
http://bookshadow.com/weblog/2017/09/24/leetcode-baseball-game/

682. Baseball Game

You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Example 1:
Input: ["5","2","C","D","+"]
Output: 30
Explanation: 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2's data was invalid. The sum is: 5.  
Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.

Example 2:
Input: ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation: 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get -2 points. The sum is: 3.
Round 3: You could get 4 points. The sum is: 7.
Operation 1: The round 3's data is invalid. The sum is: 3.  
Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
Round 5: You could get 9 points. The sum is: 8.
Round 6: You could get -4 + 9 = 5 points. The sum is 13.
Round 7: You could get 9 + 5 = 14 points. The sum is 27.

Note:
The size of the input list will be between 1 and 1000.
Every integer represented in the list will be between -30000 and 30000.

题目大意：
实现棒球记分牌。输入一组字符串：

数字表示分数
'+'表示当前轮次的分数等于上两轮分数之和
'D'表示当前轮次的分数等于上一轮分数加倍
'C'表示清除上一次的分数
求最终的得分总和

解题思路：
栈（Stack）
"""


class Solution(object):
    def calPoints_v0(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        history = []
        for op in ops:
            if op == 'C':
                if len(history) > 0:
                    history.pop()
            elif op == 'D':
                history.append(2 * history[-1] if len(history) > 0 else 0)
            elif op == '+':
                history.append((history[-2] if len(history) > 1 else 0) + history[-1] if len(history) > 0 else 0)
            else: # 0 ~ 9
                history.append(int(op))
        return sum(history)

    def calPoints(self, ops):
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)


solution = Solution()
print solution.calPoints(["5","2","C","D","+"])    # 30
print solution.calPoints(["5","-2","4","C","D","9","+","+"])  # 27

