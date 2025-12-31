class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        suffixMin = []
        currentMin = float("inf")
        prefixSum = 0
        maxScore = float("-inf")
        
        for value in reversed(nums):
            currentMin = min(currentMin, value)
            suffixMin.append(currentMin)
        suffixMin.reverse()
        for i in range(n - 1):
            prefixSum += nums[i]
            maxScore = max(maxScore, prefixSum - suffixMin[i + 1])

        return maxScore
