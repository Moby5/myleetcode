#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/01/22/leetcode-construct-the-rectangle/

题目描述：
LeetCode 492. Construct the rectangle

For a web developer, it is very important to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

1. The area of the rectangular web page you designed must equal to the given target area.
2. The width W should not be larger than the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.

You need to output the length L and the width W of the web page you designed in sequence.

Example:
Input: 4
Output: [2, 2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.

Note:
The given area won't exceed 10,000,000 and is a positive integer
The web page's width and length you designed must be positive integers.

题目大意：
给定矩形的面积area，返回矩形的长度L和宽度W，使得L和W的差值最小。

注意：

给定面积是正整数并且不超过10,000,000
长度和宽度必须是正整数

解题思路：

枚举法(def constructRectangle_v3)
记area的平方根为sqrt
从int(sqrt) 向 1 递减枚举宽度W，若area % W == 0，则L = area / W
"""

import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """        
        l = int(math.ceil(math.sqrt(area)))
        while area % l != 0:
            l += 1
        return [l, area / l]
    
    def constructRectangle_v2(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        l = int(math.ceil(math.sqrt(area)))
        w = area / l        
        while l * w != area:            
            l += 1
            w = area / l            
        return [l, w]
    
    def constructRectangle_v3(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        sqrt = int(math.sqrt(area))
        l, w = area, 1
        for x in range(sqrt, 0, -1):
            if area % x == 0:
                l, w = area / x, x
                break
        return [l, w]
        

test = Solution()        
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in nums:
    print n, test.constructRectangle(n), test.constructRectangle_v2(n), test.constructRectangle_v3(n)
