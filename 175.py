#Path Crossing

"""Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise."""

from collections import Counter
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        ans = [[0,0]]
        for i in path:
            if i=="N":
                ans.append([ans[-1][0]+1,ans[-1][1]])
            elif i=="S":
                ans.append([ans[-1][0]-1,ans[-1][1]])
            elif i=="W":
                ans.append([ans[-1][0],ans[-1][1]-1])
            elif i=="E":
                ans.append([ans[-1][0],ans[-1][1]+1])
        l = [list(x) for x in set(tuple(x) for x in ans)]
        return False if len(l)==len(ans) else True
