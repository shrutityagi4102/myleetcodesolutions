#Two Out of Three

"""Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order."""

class Solution:
    def check(self,i,nums1,nums2,nums3):
        if [i in nums1, i in nums2, i in nums3].count(True) >1:
            return True
        return False
  
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return [i for i in list(set(nums1+nums2+nums3)) if self.check(i,nums1,nums2,nums3)]
