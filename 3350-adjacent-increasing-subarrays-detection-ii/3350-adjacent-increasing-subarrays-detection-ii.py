class Solution:
    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        if n <= 1:
            return n

        incEnd = [1] * n
        incStart = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                incEnd[i] = incEnd[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                incStart[i] = incStart[i + 1] + 1

        res = 1
        for k in range(n - 1):
            res = max(res, min(incEnd[k], incStart[k + 1]))

        return res
