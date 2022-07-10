#Count Items Matching a Rule

"""You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule."""

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d= {"type":0,"color":1,"name":2}
        for keys in d:
            if keys == ruleKey:
                m = d[keys]
                break
        a = [i[m] for i in items]
        count = 0
        for b in a:
            if b==ruleValue:
                count +=1
        return count
