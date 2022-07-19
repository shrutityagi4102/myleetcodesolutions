#Single Element in a Sorted Array

"""You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.""""

from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d= dict(Counter(nums))
        for keys in d:
            if d[keys]==1:
                return keys
