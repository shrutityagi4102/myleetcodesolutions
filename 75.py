#Shuffle String

"""You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string."""

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s1 = ""
        for i in range(len(s)):
            if i in indices:
                m = indices.index(i)
                s1 += s[m]
        return s1
