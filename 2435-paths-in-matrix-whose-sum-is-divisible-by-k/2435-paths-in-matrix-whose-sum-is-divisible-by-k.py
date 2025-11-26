class Solution:
    def numberOfPaths(self, grid, k):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                for remainder in range(k):
                    if dp[i][j][remainder] > 0:
                        current_sum = dp[i][j][remainder]
                        if i + 1 < m:
                            newRem = (remainder + grid[i + 1][j]) % k
                            dp[i + 1][j][newRem] += current_sum
                            dp[i + 1][j][newRem] %= MOD
                        if j + 1 < n:
                            newRem = (remainder + grid[i][j + 1]) % k
                            dp[i][j + 1][newRem] += current_sum
                            dp[i][j + 1][newRem] %= MOD

        return dp[-1][-1][0]