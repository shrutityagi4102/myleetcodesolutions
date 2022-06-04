#Subsets

"""Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order."""

import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans.append([])
        for i in range(1,len(nums)):
            l = [x for x in itertools.combinations(nums,i)]
            ans += l
        ans.append(nums)
        return ans
