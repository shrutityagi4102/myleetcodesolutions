#Sum of Digits of String After Convert

"""You are given a string s consisting of lowercase English letters, and an integer k.

First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above."""

#import string
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        d = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
        # d = {chr(i+96):i for i in range(1,27)} 
        # to generate the above sequence
        #--------------OR---------------
        #s0 = string.ascii_lowercase 
        # d = dict(enumerate(s0,1))
        #but in the above numbers are the keys
        si = 0
        for i in s:
            if d[i]>9:
                w = [int(k) for k in str(d[i])]
                si += sum(w)
            else:
                si += d[i]
        if k == 1:
            return si
        else:
            while(k!=1):
                w = [int(i) for i in str(si)]
                k -=1
                si = sum(w)
                if k==1:
                    return si
