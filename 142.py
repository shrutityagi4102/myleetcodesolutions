#Sort Characters By Frequency

"""Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them."""

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d = dict(Counter(s))
        d = sorted(d.items(), key=lambda x: x[1], reverse = True)
        ans = ""
        for keys in d:
            ans += keys[0]*keys[1]
        return ans
