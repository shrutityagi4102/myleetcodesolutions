#Maximum 69 Number

"""You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6)."""

class Solution:
    def maximum69Number (self, num: int) -> int:
        nd = [i for i in str(num)]
        if "6" in nd:
            fs = nd.index("6")
            nd[fs] = "9"
        return int("".join(nd))
