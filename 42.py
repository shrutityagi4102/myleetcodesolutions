#N-Repeated Element in Size 2N Array
"""You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times."""

from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = dict(Counter(nums))
        for keys in d:
            if d[keys]!=1:
                return keys
