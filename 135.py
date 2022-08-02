#Minimum Time to Type Word Using Special Typewriter

"""There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'. Each second, you may perform one of the following operations:

Move the pointer one character counterclockwise or clockwise.
Type the character the pointer is currently on.
Given a string word, return the minimum number of seconds to type out the characters in word."""

class Solution:
    def minTimeToType(self, word: str) -> int:
        d = {}
        for i in range(26):
            d[chr(i+97)] = i
        ans = min(d[word[0]],26-d[word[0]])+1
        for j in range(1,len(word)):
            ans += min(abs(d[word[j]]-d[word[j-1]]),26-abs(d[word[j]]-d[word[j-1]])) + 1
        return ans
