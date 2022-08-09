#Product of Array Except Self

"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""

import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        p = numpy.prod(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                ans.append(int(numpy.prod(nums[:i])*numpy.prod(nums[i+1:])))
            else:
                ans.append(p//nums[i])    
        return ans
