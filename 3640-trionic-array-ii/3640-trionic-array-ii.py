from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = float('-inf')
        prefixSum = nums[0]

        left = peak = valley = 0
        for right in range(1, n):
            prefixSum += nums[right]

            if nums[right - 1] == nums[right]:
                left = right
                prefixSum = nums[right]
            elif nums[right - 1] > nums[right]:
                if right > 1 and nums[right - 2] < nums[right - 1]:
                    peak = right - 1 
                    while left < valley:
                        prefixSum -= nums[left]
                        left += 1
                    while left + 1 < peak and nums[left] < 0:
                        prefixSum -= nums[left]
                        left += 1
            else:
                if right > 1 and nums[right - 2] > nums[right - 1]:
                    valley = right - 1 
                if left < peak < valley:
                    maxSum = max(maxSum, prefixSum)

        return maxSum
