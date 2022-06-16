#Find Numbers with Even Number of Digits

"""Given an array nums of integers, return how many of them contain an even number of digits."""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            l = len(str(i))
            if l%2==0:
                count +=1
        return count
