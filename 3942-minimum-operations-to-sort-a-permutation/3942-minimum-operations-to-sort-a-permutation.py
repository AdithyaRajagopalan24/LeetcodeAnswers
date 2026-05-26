class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zeroIndex = nums.index(0)
        minOps = n + 1

        if all((index - value) % n == zeroIndex for index, value in enumerate(nums)):
            minOps = min(minOps, zeroIndex, n - zeroIndex + 2)

        if all((index + value) % n == zeroIndex for index, value in enumerate(nums)):
            minOps = min(minOps, zeroIndex + 2, n - zeroIndex)

        return minOps if minOps <= n else -1