#Next Greater Element II

"""Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number."""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        m = max(nums)
        newnums = nums+nums
        ans = []
        for i in range(len(nums)):
            if nums[i]==m:
                ans.append(-1)
            else:
                for j in range(i+1,len(newnums)):
                    if newnums[j]>nums[i]:
                        ans.append(newnums[j])
                        break
        return ans
