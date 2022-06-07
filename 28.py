#Sign of the Product of an Array

"""There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product)."""


class Solution:
    def signFunc(self,product):
        if product==0:
            return 0
        elif product>0:
            return 1
        else:
            return -1
        
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for i in nums:
            p *= i
        return self.signFunc(p)
