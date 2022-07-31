#Count Prefixes of a Given String

"""You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.

Return the number of strings in words that are a prefix of s.

A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string."""

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        allprefixes = [s[:i] for i in range(1,len(s)+1)]
        count = 0
        for i in words:
            if i in allprefixes:
                count +=1
        return count
