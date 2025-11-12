from math import gcd, inf
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        countOnes = nums.count(1)
        if countOnes:
            return len(nums) - countOnes
        minDiff = inf
        for i in range(len(nums)):
            currentGcd = nums[i]
            for j in range(i + 1, len(nums)):
                currentGcd = gcd(currentGcd, nums[j])
                if currentGcd == 1:
                    minDiff = min(minDiff, j - i)
                    break
        return -1 if minDiff == inf else minDiff + len(nums) - 1
