#Minimum Bit Flips to Convert Number

"""A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal."""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = '{0:b}'.format(start)
        g = '{0:b}'.format(goal)
        if len(g)!= len(s):
            for i in range(max(len(s),len(g))):
                if len(s)<len(g):
                    s = "0"*(len(g)-len(s)) + s
                else:
                    g = "0"*(len(s)-len(g)) + g
        count = 0
        for a in range(len(s)):
            if s[a]!=g[a]:
                count += 1
        return count
