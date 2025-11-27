from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        infinity = 4 * 10**18
        leastVals = [infinity] * k
        prefix = 0
        finalAns = -infinity
        leastVals[0] = 0
        
        for i, val in enumerate(nums):
            prefix += val
            remainder = (i + 1) % k
            if leastVals[remainder] != infinity:
                finalAns = max(finalAns, prefix - leastVals[remainder])
            if prefix < leastVals[remainder]:
                leastVals[remainder] = prefix
        return finalAns