#Transpose Matrix

"""Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices."""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        l = len(matrix[0])
        m = 0
        while m!=l:
            s = []
            for i in range(len(matrix)):
                s.append(matrix[i][m])
            ans.append(s)
            m +=1
        return ans
