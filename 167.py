#Count Elements With Strictly Smaller and Greater Elements

"""Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums."""

class Solution:
    def countElements(self, nums: List[int]) -> int:
        return len(nums)-len([i for i in nums if i==min(nums) or i==max(nums)])
