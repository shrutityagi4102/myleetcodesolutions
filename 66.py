#Occurrences After Bigram

"""Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third"."""

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        l = text.split(" ")
        ans = []
        for i in range(len(l)-1):
            if l[i] == first and l[i+1] == second and i!=len(l)-2:
                ans.append(l[i+2])
        return ans
