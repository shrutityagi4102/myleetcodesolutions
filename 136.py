#Complex Number Multiplication

"""A complex number can be represented as a string on the form "real+imaginaryi" where:

real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications."""

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1,b1 = num1.split("+")
        a2,b2 = num2.split("+")
        b1n = b1[:-1]
        b2n= b2[:-1]
        return str((int(a1)*int(a2))-(int(b1n)*int(b2n)))+"+"+str((int(b1n)*int(a2))+(int(b2n)*int(a1)))+"i"
