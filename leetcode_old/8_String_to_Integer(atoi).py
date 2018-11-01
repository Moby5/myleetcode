#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/01/22/leetcode-string-to-integer-atoi/

[LeetCode] 6. String to Integer (atoi)
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases.
If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters,
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

题目大意：
实现atoi函数将字符串转换为整数。

提示：仔细考虑所有输入用例。如果想给自己挑战，请不要看下面的内容并询问自己所有可能的输入用例。
注意：这道题有意描述地比较含糊（亦即，没有给出输入用例）。你需要自己发掘所有的输入要求。

atoi的要求：
函数首先尽可能多的丢弃空白字符，直到发现第一个非空字符位为止。 接着从这个字符开始，读入一个可选的正负号，然后尽可能多的读入数字，最后将它们解析成数值。
字符串中在合法数字后可以包含额外的非法字符，对于这些字符只需丢弃即可。
如果字符串的非空字符不是一个有效的整数，或者，当字符串为空或者只包含空白字符时，不需要执行转换。
如果不能够执行有效的转换则返回0。如果得到的数值超出了整数范围，返回INT_MAX (2147483647) 或者 INT_MIN (-2147483648)。

解题思路：
字符串处理，参考atoi的要求即可。
"""


'''
/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    str = str.trim();
    var ans = 0;
    var start = Number(['+', '-'].indexOf(str[0]) >= 0);
    for (var i = start; i < str.length; i++) {
        if ('0' > str[i] || str[i] > '9') break;
        ans = ans * 10 + Number(str[i] - '0');
    }
    if (str[0] == '-')
        return Math.max(-ans, -0x80000000);
    return Math.min(ans, 0x7FFFFFFF);
};

'''


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        ans = 0
        start = 0
        for i in range(len(str)):
            if str[i] == '+' or str[i] == '-':
                start = i + 1
                break
        for i in range(start, len(str)):
            num = int(str[i])
            if num < 0 or num > 9:
                break
            ans = ans * 10 + num
            print ans
        if str and str[0] == '-':
            return max(-ans, -0x80000000)
        return min(ans, 0x7FFFFFFF)


if __name__ == '__main__':
    solution = Solution()
    print solution.myAtoi('+-2')
