#!/usr/bin/env python
# coding=utf-8
# Date: 2018-10-30
# File: 289_Game_of_Life.py

"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

class Solution(object):
    def gameOfLife(self, board):  # 20 ms
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dx = (1, 1, 1, 0, 0, -1, -1, -1)
        dy = (1, 0, -1, 1, -1, 1, 0, -1)
        for x in range(len(board)):
            for y in range(len(board[0])):
                lives = 0
                for z in range(8):
                    nx, ny = x + dx[z], y + dy[z]
                    lives += self.getCellStatus(board, nx, ny)
                if lives + board[x][y] == 3 or lives == 3:
                    board[x][y] |= 2
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] >>= 1

    def getCellStatus(self, board, x, y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return 0
        return board[x][y] & 1
        

solution = Solution()

Input = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

Output = [
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]        

solution.gameOfLife(Input)
assert Input == Output, Input

print("Pass.")

"""
http://bookshadow.com/weblog/2015/10/04/leetcode-game-life/

题目大意：
根据维基百科的文章：“生命游戏，也被简称为生命，是一款由英国数学家约翰·霍顿康威于1970年设计的细胞自动机。”

给定一个m * n的细胞隔板，每一个细胞拥有一个初始状态：存活(1)或者死亡(0)。每一个细胞与其周围的8个邻居细胞（水平，竖直，对角线）发生交互，依据如下四条规则（摘自维基百科）：

任何相邻存活细胞数小于2个的存活细胞都会死亡，模拟人口不足。
任何相邻存活细胞数为2个或者3个的存活细胞会存活到下一代。
任何相邻存活细胞数大于3个的存活细胞都会死亡，模拟人口过载。
任何相邻存活细胞数等于3个的死亡细胞都会成为一个存活细胞，模拟繁殖。
编写函数，根据隔板的当前状态，计算其下一个状态（一次更新之后）

进一步思考：

你可以就地完成题目吗？记住隔板需要同时更新：你不能先更新某些细胞然后再以其变更后的值来更新其他细胞。
在这个问题中，我们使用2维数组表示隔板。原则上，隔板是无穷的，这可能导致一些边界问题。你怎么处理边界问题？
解题思路：
位运算（bit manipulation）

由于细胞只有两种状态0和1，因此可以使用二进制来表示细胞的生存状态

更新细胞状态时，将细胞的下一个状态用高位进行存储

全部更新完毕后，将细胞的状态右移一位
"""
        
