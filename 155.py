#Top K Frequent Elements

"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order."""

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict(Counter(nums))
        d1 = sorted(d.items(), key=lambda x: x[1], reverse=True)
        d1keys = [i[0] for i in d1]
        ans = []
        for i in range(k):
            ans.append(d1keys[i])
        return ans
