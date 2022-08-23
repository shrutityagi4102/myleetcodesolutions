#Intersection of Two Arrays II

"""Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order."""

from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = dict(Counter(nums1))
        d2 = dict(Counter(nums2))
        ck = list(set(d1.keys()) & set(d2.keys()))
        ans = []
        for i in ck:
            m = min(d1[i],d2[i])
            for j in range(m):
                ans.append(i)
        return ans
