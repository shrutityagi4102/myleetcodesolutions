#Special Positions in a Binary Matrix

"""Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed)."""

from collections import Counter
class Solution:
    def rowzero(self,i):
        d = dict(Counter(i))
        return True if d[1] == 1 else False
    
    def colzero(self,col):
        d = dict(Counter(col))
        return True if d[1] == 1 else False
            
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        for i in mat:
            for j in range(len(i)):
                if i[j] == 1:
                    if self.rowzero(i) and self.colzero([k[j] for k in mat]):
                        count += 1
        return count
        
