from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        charCount = Counter(s)
        maxCount = [0, 0]
        for ch, count in charCount.items():
            index = ((1 << (ord(ch) - 97)) & 0x104111) != 0
            maxCount[index] = max(maxCount[index], count)
        return maxCount[0] + maxCount[1]
