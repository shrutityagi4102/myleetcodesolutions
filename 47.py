#Merge Strings Alternately

"""You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string."""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1),len(word2))
        s = ""
        for i in range(m):
            s += word1[i]
            s += word2[i]
            
        if len(word1)==len(word2):
            return s
        elif len(word1)>len(word2):
            s += word1[m:]
            return s
        else:
            s += word2[m:]
            return s
