#Count Negative Numbers in a Sorted Matrix

"""Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid."""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = []
        for j in [i for i in grid]:
            ans += [k for k in j if k<0]
        return len(ans)
