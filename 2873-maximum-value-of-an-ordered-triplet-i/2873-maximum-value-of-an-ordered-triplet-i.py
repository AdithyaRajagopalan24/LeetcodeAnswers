class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        maxRes = 0
        maxVal = nums[0]
        maxDifference = 0
        for i in range(1, n):
            maxRes = max(maxRes , maxDifference * nums[i])
            maxDifference = max(maxDifference , maxVal - nums[i])
            maxVal = max(maxVal , nums[i])
        return maxRes