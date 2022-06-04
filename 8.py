#Count Odd Numbers in an Interval Range

"""Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive)."""

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high-low>1:
            if low%2==0:
                count = ((high-low)+1)//2
            else:
                count = ((high-low)//2) + 1
        elif high-low==1:
            count = 1
        else:
            if low%2==0:
                count = 0
            else:
                count = 1
        return count
