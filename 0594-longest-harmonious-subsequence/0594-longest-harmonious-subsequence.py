from typing import List

class Solution:
    @staticmethod
    def findLHS(nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_len = 0
        l = 0
        for r in range(n):
            x = nums[r]
            while l < r and nums[l] < x - 1:
                l += 1
            if nums[l] == x - 1:
                max_len = max(max_len, r - l + 1)
        return max_len
