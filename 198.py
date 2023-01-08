#Search a 2D Matrix II

"""Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom."""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        f = []
        for i in matrix:
            f += i
        return True if target in f else False
