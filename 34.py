#Matrix Diagonal Sum

"""Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal."""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        p,s = 0,0
        if len(mat)%2!=0:
            for i in range(len(mat)):
                i1 = mat[i]
                x = i1[::-1]
                for j in range(len(i1)):
                    if i == j:
                        p += i1[j]
                for w in range(len(x)):
                    if i == w:
                        s += x[w]
                eq = len(mat)//2 + 1
                ans = p+s-mat[eq-1][eq-1]
            return ans
        else:
            for i in range(len(mat)):
                i1 = mat[i]
                x = i1[::-1]
                for j in range(len(i1)):
                    if i == j:
                        p += i1[j]
                for w in range(len(x)):
                    if i == w:
                        s += x[w]
                ans = p+s
            return ans
