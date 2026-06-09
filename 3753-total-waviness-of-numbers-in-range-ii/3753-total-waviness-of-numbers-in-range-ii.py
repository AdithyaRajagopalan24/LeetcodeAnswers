from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def countWaviness(limit: int) -> int:
            if limit <= 0:
                return 0

            digits = str(limit)
            n = len(digits)

            @cache
            def dp(pos, tight, started, prevDigit, prevDir):
                if pos == n:
                    return 1, 0

                upper = int(digits[pos]) if tight else 9
                totalCount = totalWaviness = 0

                for digit in range(upper + 1):
                    nextTight = tight and digit == upper

                    if not started:
                        if digit == 0:
                            count, waviness = dp(pos + 1, nextTight, False, 0, 0)
                        else:
                            count, waviness = dp(pos + 1, nextTight, True, digit, 0)
                    else:
                        direction = (digit > prevDigit) - (digit < prevDigit)
                        turn = prevDir and direction and prevDir != direction

                        count, waviness = dp(pos + 1, nextTight, True, digit, direction)
                        waviness += turn * count

                    totalCount += count
                    totalWaviness += waviness

                return totalCount, totalWaviness

            return dp(0, True, False, 0, 0)[1]

        return countWaviness(num2) - countWaviness(num1 - 1)