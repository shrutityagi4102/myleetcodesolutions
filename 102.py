#Arithmetic Subarrays

"""A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i."""

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            x = nums[l[i]:r[i]+1]
            x.sort()
            d = [x[i+1]-x[i] for i in range(len(x)-1)]
            if len(list(set(d))) == 1:
                ans.append(True)
            else:
                ans.append(False)
        return ans
