#Percentage of Letter in String

"""Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent."""

from collections import Counter
import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        for keys in dict(Counter(s)):
            if keys == letter:
                return math.floor((dict(Counter(s))[keys]/len(s))*(100))
        return 0
