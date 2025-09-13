from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        closed = [[float("-inf")] * (n + 1) for _ in range(k + 1)]
        open_ = [[float("-inf")] * (n + 1) for _ in range(k)]
        closed[0] = [0] * (n + 1)

        for i in range(n):
            for t in range(k):
                open_[t][i + 1] = max(open_[t][i], closed[t][i] - prices[i])
                closed[t + 1][i + 1] = max(closed[t + 1][i], open_[t][i] + prices[i])
        
        return max(closed[t][n] for t in range(k + 1))
