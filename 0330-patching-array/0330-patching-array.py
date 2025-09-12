from typing import List

class Solution:
    def minPatches(self, nums: List[int], limit: int) -> int:
        smallestMissing = 1
        patchCount = 0
        i = 0
        while smallestMissing <= limit:
            if i < len(nums) and nums[i] <= smallestMissing:
                smallestMissing += nums[i]
                i += 1
            else:
                smallestMissing += smallestMissing
                patchCount += 1
        return patchCount
