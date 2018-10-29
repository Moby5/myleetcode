#!/usr/bin/env python
# coding=utf-8
# Date: 2018-10-29
# File: 380_Insert_Delete_GetRandom.py

"""
https://leetcode.com/problems/insert-delete-getrandom-o1/

380. Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""

import random


class RandomizedSet(object):  # 84ms

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = [], {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop()
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Init an empty set.
randomSet = RandomizedSet()

# Inserts 1 to the set. Returns true as 1 was inserted successfully.
res = randomSet.insert(1)
assert res == True, res

# Returns false as 2 does not exist in the set.
res = randomSet.remove(2)
assert res == False, res

# Inserts 2 to the set, returns true. Set now contains [1,2].
res = randomSet.insert(2)
assert res == True, res1

# getRandom should return either 1 or 2 randomly.
res = randomSet.getRandom()
assert res in {1, 2}, res

# Removes 1 from the set, returns true. Set now contains [2].
res = randomSet.remove(1)
assert res == True, res 

# 2 was already in the set, so return false.
res = randomSet.insert(2)
assert res == False, res

# Since 2 is the only number in the set, getRandom always return 2.
res = randomSet.getRandom()
assert res in {2}, res

print("Pass.")

"""
https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python

http://bookshadow.com/weblog/2016/08/04/leetcode-insert-delete-getrandom-o1/
"""

