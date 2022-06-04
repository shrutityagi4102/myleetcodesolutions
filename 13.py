#Permutations

"""Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order."""

import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a = [i for i in itertools.permutations(nums)]
        return a
