#Maximum Product of Two Elements in an Array

"""Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1)."""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = 0
        for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                m = max(m,(nums[i]-1)*(nums[j]-1))
        return m
