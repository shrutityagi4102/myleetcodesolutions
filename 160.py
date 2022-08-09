#Find Three Consecutive Integers That Sum to a Given Number

"""Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array."""

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if sum([num//3-1,num//3,num//3+1])==num:
            return [num//3-1,num//3,num//3+1]
        return []
