#Find Greatest Common Divisor of Array

"""Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers."""

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        for i in range(min(nums),0,-1):
            if min(nums)%i == 0 and max(nums)%i==0:
                return i
