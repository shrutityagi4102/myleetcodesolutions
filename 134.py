#Smallest Index With Equal Value

"""Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.

x mod y denotes the remainder when x is divided by y."""

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        match = [i%10 for i in range(len(nums))]
        right = [i for i in range(len(nums)) if nums[i]%10==match[i]]
        return right[0] if len(right)>0 else -1
