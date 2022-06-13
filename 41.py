#Sort Array By Parity

"""Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition."""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e , o = [], []
        for i in nums:
            if i%2 == 0:
                e.append(i)
            else:
                o.append(i)
        return e+o
