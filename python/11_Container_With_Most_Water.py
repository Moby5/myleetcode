#!/usr/bin/env python
# coding=utf-8
# Date: 2018-10-09

"""
https://leetcode.com/problems/container-with-most-water/description/

11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

class Solution(object):
    def maxArea(self, height):  # 68 ms
        """
        :type height: List[int]
        :rtype: int
        """
        ans, l, r = 0, 0, len(height) - 1
        while l < r:
            ans = max(ans, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
        
    def maxArea_v0(self, height):   # Time Limit Exceeded
        """
        :type height: List[int]
        :rtype: int
        """
        ans = []
        size = len(height)
        for i in range(size):
            for j in range(i, size):
                ans.append((j - i) * min(height[i], height[j]))
        return max(ans)
        
solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
expected_output = 49
output = solution.maxArea(height)
assert expected_output == output, output
print("ok")

"""
https://leetcode.com/problems/container-with-most-water/solution/

Summary
We have to maximize the Area that can be formed between the vertical lines using the shorter line as length and the distance between the lines as the width of the rectangle forming the area.

Solution


Approach 1: Brute Force
Algorithm

In this case, we will simply consider the area for every possible pair of the lines and find out the maximum area out of those.
public class Solution {
    public int maxArea(int[] height) {
        int maxarea = 0;
        for (int i = 0; i < height.length; i++)
            for (int j = i + 1; j < height.length; j++)
                maxarea = Math.max(maxarea, Math.min(height[i], height[j]) * (j - i));
        return maxarea;
    }
}

Complexity Analysis

Time complexity : O(n^2)O(n
2
). Calculating area for all \dfrac{n(n-1)}{2}
2
n(n−1)
​
 height pairs.
Space complexity : O(1)O(1). Constant extra space is used. 


Approach 2: Two Pointer Approach
Algorithm

The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. Further, the farther the lines, the more will be the area obtained.

We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. Futher, we maintain a variable maxareamaxarea to store the maximum area obtained till now. At every step, we find out the area formed between them, update maxareamaxarea and move the pointer pointing to the shorter line towards the other end by one step.

The algorithm can be better understood by looking at the example below:

1 8 6 2 5 4 8 3 7
7 / 8
How this approach works?

Initially we consider the area constituting the exterior most lines. Now, to maximize the area, we need to consider the area between the lines of larger lengths. If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line. But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the reduction in the width. This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction.

For further clarification click here and for the proof click here.

public class Solution {
    public int maxArea(int[] height) {
        int maxarea = 0, l = 0, r = height.length - 1;
        while (l < r) {
            maxarea = Math.max(maxarea, Math.min(height[l], height[r]) * (r - l));
            if (height[l] < height[r])
                l++;
            else
                r--;
        }
        return maxarea;
    }
}

Complexity Analysis

Time complexity : O(n)O(n). Single pass.

Space complexity : O(1)O(1). Constant space is used.
"""

