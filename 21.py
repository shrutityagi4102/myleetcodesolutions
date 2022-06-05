#Missing Number

"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = max(nums)
        for i in range(m+1):
            if i not in nums:
                return i
        return m+1
