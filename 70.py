#Valid Palindrome

"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise."""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sc= "!@#$%^&*`()_+\-=\[\]{};:\\|,.<>\/?~\'\""
        s1 = s.replace(" ","")
        scw = [i for i in s1 if i not in sc]
        sa = (''.join(scw)).lower()
        if sa[::-1] == sa:
            return True
        else:
            return False
