#Largest 3-Same-Digit Number in String

"""You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists."""

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = [num[i] for i in range(len(num)-2) if num[i+1]==num[i] and num[i+2]==num[i]]
        return max(n)*3 if len(n)>0 else ""
