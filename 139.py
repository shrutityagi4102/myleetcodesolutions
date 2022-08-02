#Sort Array By Parity II

"""Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition."""

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e,o = [],[]
        for i in nums:
            e.append(i) if i%2==0 else o.append(i)
        ans = []
        for j in range(len(nums)//2):
            ans.append(e[j])
            ans.append(o[j])
        return ans
