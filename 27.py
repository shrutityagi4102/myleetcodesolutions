#Find Nearest Point That Has the Same X or Y Coordinate

"""You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2)."""

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        count = 0
        l = []
        p = []
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                count +=1
                l.append(i)
                p.append(points[i])
        md =[]
        for i in range(len(p)):
            md.append(abs(x - p[i][0])+abs(y - p[i][1]))
        ans = []
        if len(md) == 0:
            return -1
        mini = min(md)
        for x in range(len(md)):
            if md[x] == mini:
                ans.append(l[x])
        return min(ans)
