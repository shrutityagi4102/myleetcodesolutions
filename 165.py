#Minimum Cost of Buying Candies With Discount

"""A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.

The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.

For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, they can take the candy with cost 1 for free, but not the candy with cost 4.
Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies."""

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        revcost = sorted(cost)[::-1]
        pay = 0
        for i in range(len(revcost)):
            if (i+1)%3==0:
                continue
            else:
                pay += revcost[i]
        return pay
