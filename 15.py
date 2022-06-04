#Reverse String

"""Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory."""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        
#We use s[:] as it is inplace s = is not inplace
