#Divide Array Into Equal Pairs

"""You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false."""

from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for i in dict(Counter(nums)).values():
            if i%2!=0:
                return False
        return True
