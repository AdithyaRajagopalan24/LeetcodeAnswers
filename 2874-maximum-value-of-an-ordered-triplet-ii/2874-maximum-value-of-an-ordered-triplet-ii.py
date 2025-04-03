import typing

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        leftMaximum = [0] * n
        leftMaximum[0] = nums[0]
        for i in range(1, n):
            leftMaximum[i] = max(leftMaximum[i - 1], nums[i])
        rightMaximum = [0] * n
        rightMaximum[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            rightMaximum[i] = max(rightMaximum[i + 1], nums[i])
        ans = 0
        for i in range(1, n - 1):
            left = leftMaximum[i - 1]
            right = rightMaximum[i + 1]
            ans = max(ans, (left - nums[i]) * right)
        return ans