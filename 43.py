#Squares of a Sorted Array

"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [i*i for i in nums]
        return sorted(squares)
