#First Unique Character in a String

"""Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1."""

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        sq = [i for i in s]
        d = dict(Counter(sq))
        k = [keys for keys in d if d[keys]==1]
        if len(k)==0:
            return -1
        for i in range(len(s)):
            if s[i] == k[0]:
                return i
        return -1

