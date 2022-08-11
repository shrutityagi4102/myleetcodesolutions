#Longer Contiguous Segments of Ones than Zeros

"""Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's."""

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        return True if len(max(s.split("0")))>len(max(s.split("1"))) else False
