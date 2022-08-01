#Check if All A's Appears Before All B's

"""Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false."""

class Solution:
    def checkString(self, s: str) -> bool:
        s.lower()
        a,b = [],[]
        for i in range(len(s)):
            if s[i] == "a":
                a.append(i)
            else:
                b.append(i)
        if len(a)==0 or len(b)==0:
            return True
        if min(b)<max(a):
            return False
        return True
