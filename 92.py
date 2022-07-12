#Count Good Triplets

"""Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets"""

import itertools
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        l = [list(j) for j in itertools.combinations(arr,3)]
        count = 0
        for i in l:
            if abs(i[0]-i[1])<=a and abs(i[1]-i[2])<=b and abs(i[0]-i[2])<=c:
                count +=1
        return count
