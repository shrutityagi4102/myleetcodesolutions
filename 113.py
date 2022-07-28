#Counting Words With a Given Prefix

"""You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s."""

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([i for i in words if i[:len(pref)]==pref])
