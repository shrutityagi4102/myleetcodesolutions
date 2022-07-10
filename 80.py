#Sum of All Odd Length Subarrays

"""Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array."""

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = []
        for i in range(len(arr)):
            imm = []
            for k in range(i,len(arr)):
                imm.append(arr[k])
                if len(imm)%2!=0:
                    s.append(sum(imm))
        return sum(s)
