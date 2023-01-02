#XOR Operation in an Array

"""You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums."""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        ans = nums[0]
        for i in range(1,len(nums)):
            a = nums[i]
            ans = ans^a
        return ans
