# Count Number of Pairs With Absolute Difference K

"""Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0."""

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[j]-nums[i])==k:
                    ans +=1
        return ans
