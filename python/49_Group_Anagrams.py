#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-27

"""
https://leetcode.com/problems/group-anagrams/description/

49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

from collections import Counter
from collections import defaultdict
import string

class Solution(object):       
    def groupAnagrams(self, strs):  # 120 ms
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
        
    def groupAnagrams_v2(self, strs):  # 280 ms
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        all_chars = string.ascii_lowercase
        for s in strs:
            count = [s.count(ch) for ch in all_chars]
            ans[tuple(count)].append(s)
        return ans.values()
        
    def groupAnagrams_v1(self, strs):  # 120 ms
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)  # list is unhashable, so transform to tuple
        return ans.values()
        
    def groupAnagrams_v0(self, strs):  # 1724 ms
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        counters, counter_cnt = [], 0
        for s in strs:
            curr_counter = Counter(s)
            if counters.count(curr_counter) > 0:  
                cidx = counters.index(curr_counter)
                ans[cidx].append(s)
            else:
                counters.append(curr_counter)
                counter_cnt += 1
                ans.append([s])
        return ans

solution = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
expected_output = [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

output = solution.groupAnagrams(strs)
print(output)

"""
https://leetcode.com/problems/group-anagrams/solution/

Approach 1: Categorize by Sorted String
Intuition

Two strings are anagrams if and only if their sorted strings are equal.

Algorithm

Maintain a map ans : {String -> List} where each key \text{K}K is a sorted string, and each value is the list of strings from the initial input that when sorted, are equal to \text{K}K.

In Java, we will store the key as a string, eg. code. In Python, we will store the key as a hashable tuple, eg. ('c', 'o', 'd', 'e').

Anagrams


Complexity Analysis

Time Complexity: O(NK \log K)O(NKlogK), where NN is the length of strs, and KK is the maximum length of a string in strs. The outer loop has complexity O(N)O(N) as we iterate through each string. Then, we sort each string in O(K \log K)O(KlogK) time.

Space Complexity: O(NK)O(NK), the total information content stored in ans. 


Approach 2: Categorize by Count
Intuition

Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same.

Algorithm

We can transform each string \text{s}s into a character count, \text{count}count, consisting of 26 non-negative integers representing the number of \text{a}a's, \text{b}b's, \text{c}c's, etc. We use these counts as the basis for our hash map.

In Java, the hashable representation of our count will be a string delimited with '#' characters. For example, abbccc will be #1#2#3#0#0#0...#0 where there are 26 entries total. In python, the representation will be a tuple of the counts. For example, abbccc will be (1, 2, 3, 0, 0, ..., 0), where again there are 26 entries total.

Anagrams


Complexity Analysis

Time Complexity: O(NK)O(NK), where NN is the length of strs, and KK is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.

Space Complexity: O(NK)O(NK), the total information content stored in ans.
"""

