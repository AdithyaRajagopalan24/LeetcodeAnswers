class Solution(object):
    def maxProfit(self, prices):
        max = 0
        start = prices[0]
        priceLen = len(prices)
        for i in range(0 , priceLen):
            if start < prices[i]: 
                max += prices[i] - start
            start = prices[i]
        return max