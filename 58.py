#Factorial Trailing Zeroes

"""Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1."""

class Solution:
    def factorial(self,no: int):
        if no<2:
            return 1
        else:
            fact = 1
            return no*factorial(no-1)
    def trailingZeroes(self, n: int) -> int:
        f = str(self.factorial(n))
        if n==0:
            return 0
        f1 = f[::-1]
        count = 0
        for i in f1:
            if int(i)==0:
                count +=1
            else:
                return count
