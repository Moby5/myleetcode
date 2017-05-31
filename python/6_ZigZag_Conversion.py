#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/08/12/leetcode-zigzag-conversion/

6. ZigZag Conversion
题目描述：
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

题目大意：
在行数给定时，字符串“PAYPALISHIRING”的Z字形（zigzag）写法像这样：（使用等宽字体可以得到更好的显示效果）：
P   A   H   N
A P L S I I G
Y   I   R
然后一行一行的读取：“PAHNAPLSIIGYIR”
编写代码读入字符串以及行数，将字符串转化为其Z字形式：
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3)应当返回“PAHNAPLSIIGYIR”。

解题思路：
模拟题，使用长度为numRows的数组按行存储经过zigzag转化后的字母
最后将每一行的字母顺次拼接即可

("PAYPALISHIRING", 4):
P   I   N
A L S I G
Y A H R
P   I
"""

import operator


class Solution(object):
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        zigzag = [[] for x in range(numRows)]
        row, step = 0, 1
        for c in s:
            zigzag[row] += c
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(reduce(operator.add, zigzag))


if __name__ == '__main__':
    solution = Solution()
    print solution.convert("PAYPALISHIRING", 3)  # PAHNAPLSIIGYIR
    print solution.convert("PAYPALISHIRING", 4)  # PINALSIGYAHRPI
