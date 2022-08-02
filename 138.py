#Shortest Distance to a Character

"""Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function."""

class Solution:
    def least(self,i,cind):
        ans = []
        for j in cind:
            ans.append(abs(j-i))
        return min(ans)
    def shortestToChar(self, s: str, c: str) -> List[int]:
        cind = [i for i in range(len(s)) if s[i]==c]
        inds = []
        for k in range(len(s)):
            inds.append(self.least(k,cind))
        return inds
