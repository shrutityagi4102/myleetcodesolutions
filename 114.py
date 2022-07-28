#Self Dividing Numbers

"""A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right]."""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = [i for i in range(left,right+1)]
        ans = []
        for i in l:
            m = [int(j) for j in str(i)]
            count = 0
            for j in m:
                if j == 0:
                    continue
                if i%j==0:
                    count +=1
            if count == len(m):
                ans.append(i)
        return ans
