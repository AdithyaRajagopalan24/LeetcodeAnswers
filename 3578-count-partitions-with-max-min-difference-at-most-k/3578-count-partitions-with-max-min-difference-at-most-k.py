from collections import deque
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        dp[0] = 1
        prefix[0] = 1
        maxDeque = deque()
        minDeque = deque()
        left = 0

        for right in range(n):
            value = nums[right]
            while maxDeque and nums[maxDeque[-1]] <= value:
                maxDeque.pop()
            maxDeque.append(right)
            while minDeque and nums[minDeque[-1]] >= value:
                minDeque.pop()
            minDeque.append(right)
            while maxDeque and minDeque and nums[maxDeque[0]] - nums[minDeque[0]] > k:
                if maxDeque[0] == left:
                    maxDeque.popleft()
                if minDeque[0] == left:
                    minDeque.popleft()
                left += 1
            windowLeft = left
            idx = right + 1
            totalWays = prefix[idx - 1]
            if windowLeft > 0:
                totalWays -= prefix[windowLeft - 1]
            totalWays %= mod
            dp[idx] = totalWays
            prefix[idx] = (prefix[idx - 1] + dp[idx]) % mod
        return dp[n]