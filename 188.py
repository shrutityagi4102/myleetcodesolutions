#Delete Greatest Value in Each Row

"""You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above."""

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        l = len(grid[0])
        for i in range(l):
            m = []
            for r in grid:
                m.append(max(r))
                del r[r.index(max(r))]
            ans += max(m)
        return ans
