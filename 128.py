#Find All Duplicates in an Array

"""Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space."""

from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        x = dict(Counter(nums))
        return [i for i in x if x[i] !=1]
