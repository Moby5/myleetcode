#!/usr/bin/env python
# coding=utf-8

"""
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

http://bookshadow.com/weblog/2014/12/22/leetcode-majority-element/

题目大意：
给定一个长度为n的数组，寻找其中的“众数”。众数是指出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的并且数组中的众数永远存在。

解题思路：
“投票算法”，设定两个变量candidate和count。candidate保存当前可能的候选众数，count保存该候选众数的出现次数。

遍历数组num。

如果当前的数字e与候选众数candidate相同，则将计数count + 1

否则，如果当前的候选众数candidate为空，或者count为0，则将候选众数candidate的值置为e，并将计数count置为1。

否则，将计数count - 1

最终留下的候选众数candidate即为最终答案。

以上算法时间复杂度为O(n)，空间复杂度为O(1)

"""

"""
官方解析：
时间复杂度: O(n2) — 蛮力法: 依次检查每一个元素是否为众数

时间复杂度: O(n), 空间复杂度: O(n) — 哈希表: 维护一个每一个元素出现次数的哈希表, 然后找到出现次数最多的元素

时间复杂度: O(n log n) — 排序: 在排序后找出连续重复出现次数最多的元素

平均时间复杂度: O(n), 最坏复杂度: 无穷大 — 随机算法: 随机选取一个元素计算其是否为众数. 如果不是, 就重复上一步骤直到找到为止。 由于选出众数的概率 > 1 / 2, 因此期望的尝试次数 < 2

时间复杂度: O(n log n) — 分治法: 将数组拆成2半, 然后找出前一半的众数A和后一半的众数B。则全局众数要么是A要么是B。 如果 A == B, 则它自然而然就是全局众数。 如果不是, 则A和B都是候选众数, 则至多只需要检查这两个元素的出现次数即可。 时间复杂度, T(n) = T(n/2) + 2n = O(n log n).

时间复杂度: O(n) — Moore投票算法: 我们维护一个当前的候选众数和一个初始为0的计数器。遍历数组时，我们看当前的元素x:

如果计数器是0, 我们将候选众数置为 x 并将计数器置为 1
如果计数器非0, 我们根据x与当前的候选众数是否相等对计数器+1或者-1
一趟之后, 当前的候选众数就是所求众数. 时间复杂度 = O(n).
时间复杂度: O(n) — 位操作法: 我们需要32次迭代, 每一次计算所有n个数的第i位的1的个数。由于众数一定存在，那么或者1的个数 > 0的个数 或者反过来(但绝不会相同)。 众数的第i位一定是计数较多数字。
"""

from collections import Counter
from collections import defaultdict
class Solution(object):    
    def majorityElement(self, nums):  # my solution
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common(1)[0][0]
    
    def majorityElement_v1(self, nums):  # my solution
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        return sorted(dic.iteritems(), key=lambda x: x[1], reverse=True)[0][0]    
    
    def majorityElement_v2(self, num):
        candidate, count = None, 0
        for e in num:
            if count == 0:
                candidate, count = e, 1
            elif e == candidate:
                count += 1
            else:
                count -= 1
        return candidate    
        
test = Solution()        
print test.majorityElement([1])
print test.majorityElement([2, 3, 4, 2, 3, 2, 2])

