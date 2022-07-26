#Capitalize the Title

"""You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:

If the length of the word is 1 or 2 letters, change all letters to lowercase.
Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title."""

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        t = title.split(" ")
        ans = []
        for j in t:
            if len(j)==1 or len(j)==2:
                j = j.lower()
            else:
                j = j.lower()
                j = j.capitalize()
            ans.append(j)
        return " ".join(ans)
