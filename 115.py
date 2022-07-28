#Check if All Characters Have Equal Number of Occurrences

"""Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency)."""

from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = dict(Counter([i for i in s]))
        l = list(set(d.values()))
        if len(l)==1:
            return True
        return False
