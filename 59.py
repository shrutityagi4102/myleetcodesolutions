#Add Digits

"""Given an integer num, repeatedly add all its digits until the result has only one digit, and return it."""

class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        while num>9:
            l = [int(i) for i in str(num)]
            num = sum(l)
        return num
