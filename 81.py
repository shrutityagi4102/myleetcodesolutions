#Decode the Message

"""You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message."""

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        s = [i for i in key if i!=" "]
        s1 = []
        [s1.append(x) for x in s if x not in s1]
        ch = "a"
        d = {}
        for i in s1:
            d[i] = ch
            j = ord(ch)
            ch = chr(j+1)
        m = [i for i in message]
        ans = ""
        for i in m:
            if i == " ":
                ans += " "
            else:
                for keys in d:
                    if i == keys:
                        ans+=d[i]
        return ans
