#Minimum Index Sum of Two Lists

"""Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer."""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        if len(list1)>len(list2):
            for i in range(len(list1)):
                for j in range(len(list2)):
                    if list1[i]==list2[j]:
                        d[list1[i]] = i+j
        elif len(list1)<len(list2):
            for i in range(len(list2)):
                for j in range(len(list1)):
                    if list2[i]==list1[j]:
                        d[list2[i]] = i+j
        else:
            for i in range(len(list1)):
                for j in range(len(list2)):
                    if list1[i]==list2[j]:
                        d[list1[i]] = i+j
        ims = [d[keys] for keys in d]
        minu = min(ims)
        ans = [keys for keys in d if d[keys] == minu]
        return ans
