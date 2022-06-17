#Jewels and Stones

"""You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A"."""

from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = [i for i in stones]
        d = dict(Counter(s))
        j = [j for j in jewels]
        count = 0
        for keys in d:
            for m in j:
                if m == keys:
                    count+= d[keys]
        return count
