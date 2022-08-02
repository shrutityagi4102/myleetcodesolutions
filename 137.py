#Maximum Number of Words You Can Type

"""There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard."""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        t = text.split()
        typed = len(t)
        for i in t:
            for j in i:
                if j in brokenLetters:
                    typed -= 1
                    break
        return typed
