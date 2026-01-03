class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        prevWays1, prevWays2 = 3, 12
        for _ in range(n - 1):
            prevWays2, prevWays1 = 5 * prevWays2 - 2 * prevWays1, prevWays2
        return prevWays2 % mod
