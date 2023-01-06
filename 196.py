#Number of Common Factors

"""Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b."""

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a!= 1 :
            z = [1,a]
        else:
            z = [1]
        divisors = [x for x in range(2, a//2+1) if a%x == 0]+z
        if b!= 1 :
            z = [1,b]
        else:
            z = [1]
        divisors1 = [x for x in range(2, b//2+1) if b%x == 0]+z
        return len([j for j in divisors if j in divisors1])
