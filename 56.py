# Reverse Integer

"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""

import math
class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            s = str(x)
            s1 = s[::-1]
            sino  = int(s1)
            if sino<=(math.pow(2,31)-1) and sino>=(-(math.pow(2,31))):
                return sino
            else:
                return 0
        else:
            s = str(abs(x))
            s1 = s[::-1]
            sino = int(s1)
            if sino<=(math.pow(2,31)-1) and sino>=(-(math.pow(2,31))):
                return -sino
            else:
                return 0
