class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)

        def needsMoreThanM(maxSum):
            parts = 1
            currentSum = 0

            for num in nums:
                if currentSum + num > maxSum:
                    currentSum = num
                    parts += 1
                else:
                    currentSum += num

            return parts > m

        while left < right:
            mid = (left + right) // 2

            if needsMoreThanM(mid):
                left = mid + 1
            else:
                right = mid

        return left