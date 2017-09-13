#!/bin/bash

:<<!
195. Tenth Line

How would you print just the 10th line of a file?
For example, assume that file.txt has the following content:
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10

Your script should output the tenth line, which is:
Line 10

Hint:
1. If the file contains less than 10 lines, what should you output?
2. There's at least three different solutions. Try to explore all possibilities.

题目大意：
输出一个文件的第10行。

思考：
1. 如果文件包含内容不足10行，应该输出什么？
2. 有至少3种不同的解决方法，尝试列举所有的可能方案    
!

# Read from the file file.txt and output the tenth line to stdout.
# 解法一，使用awk
awk 'NR == 10' file.txt

# 解法二，使用sed
# sed -n '10p' file.txt

# 解法三，组合使用tail与head
# tail -n+10 file.txt | head -n1

# 另外，以下这种方法不符合要求
# head file.txt -n10 | tail -n1 # 因为如果文件包含内容不足10行，会输出最后一行
