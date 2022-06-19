#Greatest English Letter in Upper and Lower Case

"""Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

An English letter b is greater than another letter a if b appears after a in the English alphabet."""

class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = []
        for i in s:
            if i.isupper():
                if i.lower() in s:
                    ans.append(i)
            if i.islower():
                if i.upper() in s:
                    ans.append(i.upper())
        if len(ans) == 0:
            return ""
        else:
            return max(ans)
                
