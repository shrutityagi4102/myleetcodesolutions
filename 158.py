#String Matching in an Array

"""Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j]."""

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in words:
            for j in words:
                if i !=j:
                    if i in j and i not in ans:
                        ans.append(i)
        return ans
