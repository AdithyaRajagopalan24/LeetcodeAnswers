class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        dp = triangle[-1][:]

        for row in range(rows - 2, -1, -1):
            for col in range(row + 1):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        return dp[0]