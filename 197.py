#Count Number of Distinct Integers After Reverse Operations

"""You are given an array nums consisting of positive integers.

You have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.

Return the number of distinct integers in the final array."""

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = nums + [int(str(i)[::-1]) for i in nums]
        return len(set(n))
