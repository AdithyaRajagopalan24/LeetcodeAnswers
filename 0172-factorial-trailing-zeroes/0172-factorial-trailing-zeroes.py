class Solution:
    def trailingZeroes(self, n: int) -> int:
        fivesCount = 0
        i = 5
        while i <= n:
            fivesCount += n // i
            i *= 5
        return fivesCount