#!/usr/bin/env python
# coding=utf-8
# Date: 2018-11-02
# File: 240_Search_a_2D_Matrix_II.py

"""
https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):  # 48ms
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix) or not len(matrix[0]):
            return False
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False
        
    def searchMatrix_v1(self, matrix, target):  # 二分查找 148ms
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix) or not len(matrix[0]):
            return False
        y = len(matrix[0]) - 1
        
        def binary_search(nums, low, high):
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return high

        for x in range(len(matrix)):
            y = binary_search(matrix[x], 0, y)
            if matrix[x][y] == target:
                return True
        return False        
        
    def searchMatrix_v2(self, matrix, target):  # 48ms
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix) or not len(matrix[0]):
            return False
        y = len(matrix[0]) - 1
        for x in range(len(matrix)):
            while y and matrix[x][y] > target:
                y -= 1
            if matrix[x][y] == target:
                return True
        return False

        
solution = Solution()

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]      

target = 5
output = True
pred = solution.searchMatrix(matrix, target)
assert pred == output, pred
  
target = 20   
output = False
pred = solution.searchMatrix(matrix, target)
assert pred == output, pred

target = 4  
output = True
pred = solution.searchMatrix(matrix, target)
assert pred == output, pred

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
target = 19
output = True
pred = solution.searchMatrix(matrix, target)
assert pred == output, pred

print("Pass.")

"""
http://bookshadow.com/weblog/2015/07/23/leetcode-search-2d-matrix-ii/

题目大意：
编写一个高效的算法，从一个m × n矩阵中寻找一个值。矩阵具有如下性质：

每一行的整数从左向右递增
每一列的整数从上往下递增

测试样例见题目描述。

解题思路：


O(m + n)解法：
从矩阵的右上角(屏幕坐标系）开始，执行两重循环
外循环递增枚举每行，内循环递减枚举列

Python代码：
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        y = len(matrix[0]) - 1
        for x in range(len(matrix)):
            while y and matrix[x][y] > target:
                y -= 1
            if matrix[x][y] == target:
                return True
        return False
        
        
O(m * logn)解法：
循环枚举行，二分查找列

Python代码：
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        y = len(matrix[0]) - 1
        def binSearch(nums, low, high):
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return high
        for x in range(len(matrix)):
            y = binSearch(matrix[x], 0, y)
            if matrix[x][y] == target:
                return True
        return False


O(n ^ 1.58)解法：
参考：https://leetcode.com/discuss/47528/c-with-o-m-n-complexity

分治法，以矩形中点为基准，将矩阵拆分成左上，左下，右上，右下四个区域

若中点值 < 目标值，则舍弃左上区域，从其余三个区域再行查找

若中点值 > 目标值，则舍弃右下区域，从其余三个区域再行查找

时间复杂度递推式：T(n) = 3T(n/2) + c

相关博文：http://articles.leetcode.com/2010/10/searching-2d-sorted-matrix-part-ii.html

Java代码：
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n=matrix.length, m=matrix[0].length;
        return helper(matrix,0,n-1,0,m-1,target);
    }
    boolean helper(int[][] matrix, int rowStart, int rowEnd, int colStart, int colEnd, int target ){
        if(rowStart>rowEnd||colStart>colEnd){
            return false;
        }
        int rm=(rowStart+rowEnd)/2, cm=(colStart+colEnd)/2;
        if(matrix[rm][cm]== target){
            return true;
        }
        else if(matrix[rm][cm] >target){
            return helper(matrix, rowStart, rm-1,colStart, cm-1,target)||
                helper(matrix,  rm, rowEnd, colStart,cm-1,target) ||
                helper(matrix, rowStart, rm-1,cm, colEnd,target);
        }
        else{
            return helper(matrix, rm+1, rowEnd, cm+1,colEnd,target)||
                helper(matrix,  rm+1, rowEnd, colStart,cm,target) ||
                helper(matrix, rowStart, rm,cm+1, colEnd,target);
        }
    
}

https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/183609/An-intelligible-Python-solution-beats-99.64-48ms
"""

