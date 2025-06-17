import math

class Solution:
    def countGoodArrays(self, arrayLength: int, valueLimit: int, fixedCount: int) -> int:
        freePositions = arrayLength - fixedCount
        mod = int(1e9) + 7
        waysToFillFree = (valueLimit * pow(valueLimit - 1, freePositions - 1, mod)) % mod
        totalWays = waysToFillFree * math.comb(freePositions + fixedCount - 1, freePositions - 1)
        totalWays %= mod
        return int(totalWays)
