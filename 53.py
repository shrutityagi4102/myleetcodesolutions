#Check If All 1's Are at Least Length K Places Away

"""Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false."""

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        o = [i for i in range(len(nums)) if nums[i]==1]
        for j in range(len(o)-1):
            if o[j+1]-o[j]>k:
                continue
            else:
                return False
        return True
