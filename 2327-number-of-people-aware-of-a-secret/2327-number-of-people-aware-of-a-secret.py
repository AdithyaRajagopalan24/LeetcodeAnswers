class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1

        for day in range(2, n + 1):
            if day - delay >= 1:
                dp[day] += 1
            for start in range(max(1, day - forget + 1), max(1, day - delay) + 1):
                dp[day] = (dp[day] + dp[start]) % MOD
            if day - forget >= 1:
                dp[day] -= 1

        return dp[n] % MOD
