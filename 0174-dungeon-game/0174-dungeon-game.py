from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [float("inf")] * (cols + 1)
        dp[cols - 1] = 1
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j])
        return dp[0]
