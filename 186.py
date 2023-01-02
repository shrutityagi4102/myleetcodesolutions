#Count the Digits That Divide a Number

"""Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0."""

class Solution:
    def countDigits(self, num: int) -> int:
        digs = [int(i) for i in str(num)]
        count  = 0
        for i in digs:
            if num%i == 0:
                count += 1
        return count
