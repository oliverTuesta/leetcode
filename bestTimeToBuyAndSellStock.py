# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Number: 121

class Solution(object):
    def maxProfit(self, prices):
        cheapest = prices[0]
        maxProfit = 0
        for i in prices:
            if i < cheapest:
                cheapest = i
            else: 
                p = i - cheapest
                maxProfit = max(p, maxProfit)
        return maxProfit
