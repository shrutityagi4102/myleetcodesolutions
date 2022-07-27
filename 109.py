#Determine if String Halves Are Alike

"""You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false."""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        v = ["a","e","i","o","u"]
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        x = [i for i in a if i in v]
        y = [i for i in b if i in v]
        if len(x)==len(y):   
             return True
        return False
