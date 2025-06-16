class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxVal, maxDiff = nums[-1], -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < maxVal:
                maxDiff = max(maxDiff, maxVal - nums[i])
            maxVal = max(maxVal, nums[i])
        return maxDiff