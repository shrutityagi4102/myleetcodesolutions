#Convert Integer to the Sum of Two No-Zero Integers

"""No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [A, B] where:

A and B are No-Zero integers.
A + B = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions you can return any of them."""

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n==2:
            return [1,1]
        else:
            x = 2
            y = n-2
            while "0" in str(y) or "0" in str(x):
                y -=1
                x +=1
            return [x,y]
