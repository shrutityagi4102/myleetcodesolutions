#Sum of Unique Elements

"""
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
"""

from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = dict(Counter(nums))
        un = [i for i in d if d[i]==1]
        return sum(un)
