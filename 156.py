#Count Integers With Even Digit Sum

"""Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits."""

class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        nums = [i for i in range(1,num+1)]
        for i in nums:
            digi = [int(j) for j in str(i)]
            if sum(digi)%2==0:
                count +=1
        return count
