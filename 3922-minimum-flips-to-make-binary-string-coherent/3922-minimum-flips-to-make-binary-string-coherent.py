from collections import Counter

class Solution:
    def minFlips(self, s: str) -> int:
        freq = Counter(s)

        if freq['1'] <= 1:
            return 0

        bothEndsOne = s[0] == '1' and s[-1] == '1'

        return min(
            freq['0'],
            freq['1'] - 1 - bothEndsOne
        )