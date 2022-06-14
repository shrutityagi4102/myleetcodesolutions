#Unique Number of Occurrences

"""Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise."""

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict(Counter(arr))
        sub = []
        for keys in d:
            if d[keys] not in sub:
                sub.append(d[keys])
                continue
            else:
                return False
        return True
