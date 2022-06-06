#Subtract the Product and Sum of Digits of an Integer

"""Given an integer number n, return the difference between the product of its digits and the sum of its digits."""

import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        l = [int(i) for i in s]
        p = math.prod(l)
        s1 = sum(l)
        return p-s1
      
# you can import numpy also
