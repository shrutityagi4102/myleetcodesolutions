#Rotate Image

"""You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation."""

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
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = self.transpose(matrix[::-1])
