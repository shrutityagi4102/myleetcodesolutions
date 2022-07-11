#Check If Two String Arrays are Equivalent

"""Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string."""

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = "".join(word1)
        w2 = "".join(word2)
        if w1==w2:
            return True
        else:
            return False
