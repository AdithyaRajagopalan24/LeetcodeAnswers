class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        def calculateCost(start, end):
            if start >= end:
                return 0
            if dp[start][end] != 0:
                return dp[start][end]
            minCost = float('inf')

            for guessVal in range((start + end) // 2, end + 1):
                cost = guessVal + max(calculateCost(start, guessVal - 1), calculateCost(guessVal + 1, end))
                if cost <= minCost:
                    minCost = cost
            dp[start][end] = minCost
            return minCost
        return calculateCost(1, n)