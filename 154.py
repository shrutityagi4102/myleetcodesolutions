#Number of Arithmetic Triplets

"""You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets."""

from itertools import combinations
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        alltrip = list(combinations(nums,3))
        return len([i for i in alltrip if i[1]-i[0]==diff and i[2]-i[1]==diff])
