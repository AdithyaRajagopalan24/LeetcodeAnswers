from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        for num in nums:
            maxOr |= num

        n = len(nums)
        memo = {}

        def dfs(currOr: int, i: int) -> int:
            if i == n:
                return int(currOr == maxOr)
            if (currOr, i) in memo:
                return memo[(currOr, i)]
            pick = dfs(currOr | nums[i], i + 1)
            skip = dfs(currOr, i + 1)
            memo[(currOr, i)] = pick + skip
            return memo[(currOr, i)]

        return dfs(0, 0)
