from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], stepValue: int) -> int:
        remainderFreq = [0] * stepValue
        
        for num in nums:
            remainder = num % stepValue
            if remainder < 0:
                remainder += stepValue
            remainderFreq[remainder] += 1

        candidate = 0
        while True:
            remainder = candidate % stepValue
            if remainderFreq[remainder] == 0:
                return candidate
            remainderFreq[remainder] -= 1
            candidate += 1
