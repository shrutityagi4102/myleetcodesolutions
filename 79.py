#Widest Vertical Area Between Two Points Containing No Points

"""Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area."""

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = [i[0] for i in points]
        x.sort()
        d = []
        for i in range(len(x)-1):
            d.append(x[i+1]-x[i])
        return max(d)
