class Solution(object):
    def checkRecord(self, n):
        mod = 10**9 + 7
        dp = [[0] * 3 for _ in range(n + 1)]
        dp[0][0] = 1     
        for i in range(1, n + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % mod
            dp[i][1] = dp[i - 1][0] % mod
            dp[i][2] = dp[i - 1][1] % mod
        total = 0
        for i in range(n):
            validLeft = (dp[i][0] + dp[i][1] + dp[i][2]) % mod
            validRight = (dp[n - i - 1][0] + dp[n - i - 1][1] + dp[n - i - 1][2]) % mod
            total = (total + validLeft * validRight) % mod
        return (total + sum(dp[n])) % mod