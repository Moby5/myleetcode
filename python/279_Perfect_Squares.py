#!/usr/bin/env python
# coding=utf-8
# Date: 2018-10-12

"""
https://leetcode.com/problems/perfect-squares/description/

279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

from collections import defaultdict

class Solution(object):

    _dp = [0]
    def numSquares(self, n):  # 动态规划优化 84 ms
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,
        return dp[n]
        
    def numSquares_v0(self, n):  # 动态规划 6216 ms
        """
        :type n: int
        :rtype: int
        """
        dp = defaultdict(int)
        y = 1
        while y * y <= n:
            dp[y * y] = 1
            y += 1
        for x in range(1, n + 1):
            y = 1
            while x + y * y <= n:
                if x + y * y not in dp or dp[x] + 1 < dp[x + y * y]:
                    dp[x + y * y] = dp[x] + 1
                y += 1
        return dp[n]

solution = Solution()

n = 12
expected_output = 3
output = solution.numSquares(n)
assert expected_output == output, output
    
n = 13
expected_output = 2
output = solution.numSquares(n)
assert expected_output == output, output

print("ok")

"""
http://bookshadow.com/weblog/2015/09/09/leetcode-perfect-squares/

题目大意：
给定一个正整数n，求相加等于n的完全平方数（例如 1, 4, 9, 16, ...）的最小个数。

例如，给定n = 12，返回3，因为12 = 4 + 4 + 4；给定n = 13，返回2，因为13 = 4 + 9。

解题思路：
解法I：数论（Number Theory）

时间复杂度：O(sqrt n)

四平方和定理(Lagrange's Four-Square Theorem)：所有自然数至多只要用四个数的平方和就可以表示。

参考链接：https://leetcode.com/discuss/56982/o-sqrt-n-in-ruby-and-c

C代码：
int numSquares(int n) {
    while (n % 4 == 0)
        n /= 4;
    if (n % 8 == 7)
        return 4;
    for (int a=0; a*a<=n; ++a) {
        int b = sqrt(n - a*a);
        if (a*a + b*b == n)
            return !!a + !!b;
    }
    return 3;
}

顺便感慨一下数论的强大（认真脸）。

解法II：动态规划（Dynamic Programming）

时间复杂度：O(n * sqrt n)

初始化将dp数组置为无穷大；令dp[y * y] = 1，其中：y * y <= n

状态转移方程：

dp[x + y * y] = min(dp[x + y * y], dp[x] + 1)
其中：dp [i] 表示凑成i所需的平方和数字的最小个数，并且 x + y * y <= n

Java代码：
public class Solution {
    public int numSquares(int n) {
        int dp[] = new int[n + 1];
        //仔细观察，不需要担心溢出
        Arrays.fill(dp, Integer.MAX_VALUE);
        for (int i = 1; i * i <= n; i++) {
            dp[i * i] = 1;
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; i + j * j <= n; j++) {
                dp[i + j * j] = Math.min(dp[i] + 1, dp[i + j * j]);
            }
        }
        return dp[n];
    }
}

相同时间复杂度的Python代码返回Time Limit Exceeded，或许是由于OJ对于Python的时间限制比较严苛。

Python代码（Time Limit Exceeded）：
class Solution(object):
    def numSquares(self, n):
        dp = collections.defaultdict(int)
        y = 1
        while y * y <= n:
            dp[y * y] = 1
            y += 1
        for x in range(1, n + 1):
            y = 1
            while x + y * y <= n:
                if x + y * y not in dp or dp[x] + 1 < dp[x + y * y]:
                    dp[x + y * y] = dp[x] + 1
                y += 1
        return dp[n]

由于该题有许多大型的测试样例，因此对于速度比较慢的编程语言，在测试样例之间共享计算结果，可以减少时间开销。

参考链接：https://leetcode.com/discuss/56993/static-dp-c-12-ms-python-172-ms-ruby-384-ms

下面的Python代码按需扩展dp数组的长度，可以通过系统测试：

Python代码（Accepted）：
class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]


"""

