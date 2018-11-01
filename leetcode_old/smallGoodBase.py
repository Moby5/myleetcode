#!/usr/bin/env python
# coding=utf-8

import math

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        for m in range(int(math.log(n, 2)), 1, -1):
            k = int(n ** (1.0 / m))
            if sum(k ** i for i in range(m + 1)) == n:
                return str(k)
            return str(n - 1)

#def smallestGoodBase(n):
#    for k in range()

if __name__ == "__main__":
    solution = Solution()
    print solution.smallestGoodBase(13)
    print


