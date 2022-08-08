#Three Consecutive Odds

"""Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false."""

class Solution:
    def allodd(self,i):
        ans = [j for j in i if j%2!=0]
        return True if len(ans)==len(i) else False
    
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        threecons = [arr[i:i+3] for i in range(len(arr)-2)]
        for i in threecons:
            if self.allodd(i):
                return True
        return False
