class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        totalSum = 0
        for i in range(k):
            currentMultiplier = max(1, mul - i)
            totalSum += nums[i] * currentMultiplier
        return totalSum