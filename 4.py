#Find First and Last Position of Element in Sorted Array

"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1]."""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        mi = -1
        ma = -1
        for i in range(len(nums)):
            if nums[i] == target:
                mi = i
        for j in range (len(nums)-1,-1,-1):
            if nums[j] == target:
                ma = j
        l = [mi,ma]
        return l[::-1]
