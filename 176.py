#Kth Missing Positive Number

"""Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array."""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = []
        i = 1
        while len(ans)<k:
            if i not in arr:
                ans.append(i)
            i += 1
        return ans[-1]
