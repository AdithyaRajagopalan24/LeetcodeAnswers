class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        return max(
            self.robLinear(nums[:-1]),
            self.robLinear(nums[1:])
        )

    def robLinear(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        maxRobAtIndexDP = [0] * n
        maxRobAtIndexDP[0] = nums[0]
        maxRobAtIndexDP[1] = max(nums[0], nums[1])

        for i in range(2, n):
            maxRobAtIndexDP[i] = max(
                maxRobAtIndexDP[i - 2] + nums[i],
                maxRobAtIndexDP[i - 1]
            )

        return maxRobAtIndexDP[-1]