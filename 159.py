#Find Lucky Integer in an Array

"""Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1."""

from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = dict(Counter(arr))
        ans = [i for i in d if i==d[i]]
        return max(ans) if len(ans) !=0 else -1
