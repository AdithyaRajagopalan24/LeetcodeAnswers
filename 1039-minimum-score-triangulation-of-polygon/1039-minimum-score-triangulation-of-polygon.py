class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        if n == 3:
            return values[0] * values[1] * values[2]
        dp = [[0] * n for _ in range(n - 1)]
        for gap in range(2, n):
            for left in range(n - gap):
                right = left + gap
                minWeight = 1 << 32
                edgeProduct = values[left] * values[right]
                for mid in range(left + 1, right):
                    minWeight = min(
                        minWeight,
                        edgeProduct * values[mid] + dp[left][mid] + dp[mid][right]
                    )
                dp[left][right] = minWeight
        return dp[0][-1]
