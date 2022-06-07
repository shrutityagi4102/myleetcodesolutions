#Can Make Arithmetic Progression From Sequence

"""A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false. """

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = []
        for i in range(len(arr)-1):
            d.append(arr[i+1]-arr[i])
        d1 = set(d)
        if len(d1)==1:
            return True
        else:
            return False
