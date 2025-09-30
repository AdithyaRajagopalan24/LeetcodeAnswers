from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        coeff = 1
        ans = 0
        for i in range(n):
            ans = (ans + coeff * nums[i]) % 10
            if i < n - 1:
                coeff = coeff * (n - 1 - i) // (i + 1)
        return ans
