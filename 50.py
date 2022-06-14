#Intersection of 2 Arrays

"""Given 2 integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order."""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums11 = list(set(nums1))
        nums21 = list(set(nums2))
        ans = []
        if len(nums11) == len(nums21):
            for i in nums11:
                if i in nums21:
                    ans.append(i)
        elif len(nums11) > len(nums21):
            for i in nums11:
                if i in nums21:
                    ans.append(i)
        else:
            for i in nums21:
                if i in nums11:
                    ans.append(i)
        return ans
