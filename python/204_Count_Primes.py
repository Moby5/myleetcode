#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-04

"""
https://leetcode.com/problems/count-primes/description/

http://bookshadow.com/weblog/2015/04/27/leetcode-count-primes/

204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

题目大意：
统计小于非负整数n的素数的个数

提示：n的范围是100,000到5,000,000

参考文献：
一共有多少个素数？(https://primes.utm.edu/howmany.html)

埃拉托斯特尼筛法 (http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

解题思路：
见埃拉托斯特尼筛法。

另请参阅：http://open.163.com/movie/2012/10/0/6/M99VJKUHC_M9ENDUB06.html

起初Python的时间限制过于严格，采用Python解题对于测试样例5000000总是返回Time Limit Exceeded，后来管理员放宽了Python的时限。
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime = [True] * max(n, 2)
        is_prime[0], is_prime[1] = False, False
        x = 2
        while x * x < n:
            if is_prime[x]:
                p = x * x
                while p < n:
                    is_prime[p] = False
                    p += x
            x += 1
        return sum(is_prime)
        
    def countPrimes_v0(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime = [True] * max(n, 2)
        is_prime[0], is_prime[1] = False, False
        for x in range(2, int(n ** 0.5) + 1):
            if is_prime[x]:
                p = x * x
                while p < n:
                    is_prime[p] = False
                    p += x
        return sum(is_prime)              


solution = Solution()
for n in [10]:
    print(n, solution.countPrimes(n))
    

"""
下面附本题目采用Java解答的代码。

Java代码：
public class Solution {
    public int countPrimes(int n) {
        boolean notPrime[] = new boolean[n + 2];
        notPrime[0] = notPrime[1] = true;
        for (int i = 2; i * i < n; i++) {
            if (!notPrime[i]) {
                int c = i * i;
                while (c < n) {
                    notPrime[c] = true;
                    c += i;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (!notPrime[i])
                ans ++;
        }
        return ans;
    }
}
"""    
        
