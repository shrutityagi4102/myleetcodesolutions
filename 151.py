#Merge Similar Items

"""You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:

items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
The value of each item in items is unique.
Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.

Note: ret should be returned in ascending order by value."""

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1val = [i[0] for i in items1]
        items2val = [i[0] for i in items2]
        ans = []
        for i in items1val:
            if i in items2val:
                items1w = items1[items1val.index(i)][1]
                items2w = items2[items2val.index(i)][1]
                ans.append([i,items1w+items2w])
            else:
                items1w = items1[items1val.index(i)][1]
                ans.append([i,items1w])
        for i in items2val:
            if i not in items1val:
                items2w = items2[items2val.index(i)][1]
                ans.append([i,items2w])
        return sorted(ans)
