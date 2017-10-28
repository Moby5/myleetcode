#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/09/18/leetcode-binary-watch/

LeetCode 401. Binary Watch

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.



For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:

The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

题目大意：
一个二进制手表顶端有4盏LED灯表示小时(0-11)，底部有6盏LED灯表示分钟(0-59)。

每一盏LED灯表示一个0或1，最右端为最低位。

例如上图中的例子读数为"3:25"。

给定一个非负整数n表示当前燃亮的LED灯数，返回所有可能表示的时间。

注意：

输出顺序不重要。

小时不可以包含前缀0，例如"01:00"是无效的，应当为"1:00"。

分钟必须包含两位数字，可以包含前导0，例如"10:2"是无效的，应当为"10:02"。

解题思路：
位运算（Bit Manipulation）

10盏灯泡的燃亮情况可以通过0-1024进行表示，然后计数二进制1的个数即可。

利用位运算将状态拆分为小时和分钟。
"""

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    ans.append('%d:%02d' % (h, m))
        return ans

    def readBinaryWatch_ref(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for x in range(1024):
            if bin(x).count('1') == num:
                h, m = x >> 6, x & 0x3F
                if h < 12 and m < 60:
                    ans.append('%d:%02d' % (h, m))
        return ans
        
    def readBinaryWatch_ref2(self, num):
        """
        :type num: int
        :rtype: List[str]
		参考LeetCode Discuss：https://discuss.leetcode.com/topic/59374/simple-python-java
		枚举小时h和分钟m，然后判断二进制1的个数是否等于num        
        """
        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h)+ bin(m)).count('1') == num:
                    ans.append('%d:%02d' % (h, m))
        return ans        
        
       
test = Solution()
print test.readBinaryWatch(1)

