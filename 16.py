#Single Number

"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space."""

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict(Counter(nums))
        for keys in d:
            if d[keys] == 1:
                return keys
