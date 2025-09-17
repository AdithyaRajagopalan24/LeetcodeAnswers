class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxGap = 0
        nums.sort()
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            maxGap = max(maxGap, diff)
        return maxGap
