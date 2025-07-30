from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxValue = max(nums)
        longestRun = 0
        runLength = 0
        for value in nums:
            if value == maxValue:
                runLength += 1
            else:
                if runLength > longestRun:
                    longestRun = runLength
                runLength = 0
        if runLength > longestRun:
            longestRun = runLength
        return longestRun