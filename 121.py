#Replace Elements with Greatest Element on Right Side

"""Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array."""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        g= []
        for i in range(len(arr)):
            if i == len(arr)-1:
                g.append(-1)
                break
            nino = arr[i+1:]
            g.append(max(nino))
        return g
