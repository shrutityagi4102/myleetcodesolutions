#Find Triangular Sum of an Array

"""You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums."""

class Solution:
    def checksum(self,nums):
        s = []
        for i in range(len(nums)-1):
            su = nums[i]+nums[i+1]
            if su >9:
                x = str(su)
                s.append(int(x[-1]))
            else:
                s.append(su)
        return s
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        ans = self.checksum(nums)
        while len(ans)!=1:
            ans = self.checksum(ans)
        return ans[0]