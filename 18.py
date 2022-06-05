#Majority Element

"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array."""

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict(Counter(nums))
        l = len(nums)//2
        x = []
        for keys in d:
            x.append(d[keys])
        m = max(x)
        for keys in d:
            if d[keys] == m:
                return keys
