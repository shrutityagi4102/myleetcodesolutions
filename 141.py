#Keyboard Row

"""Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm"."""

from collections import Counter
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        ans = []
        for i in words:
            l = [j for j in i]
            r = []
            for m in l:
                m.lower()
                if m in r1:
                    r.append(1)
                elif m in r2:
                    r.append(2)
                elif m in r3:
                    r.append(3)
            if len(list(set(r))) == 1:
                ans.append(i)
        return ans
