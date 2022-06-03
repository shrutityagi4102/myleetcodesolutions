#Element Appearing More Than 25% In Sorted Array

"""Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer."""

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = []
        for i in range(len(arr)):
            c.append(arr.count(arr[i]))
        m = c.index(max(c))
        return arr[m]
