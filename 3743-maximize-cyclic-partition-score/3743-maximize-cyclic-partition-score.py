from typing import List
import math

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minIndex = min(range(n), key=lambda i: nums[i])
        forward = [nums[(minIndex + i) % n] for i in range(n)]
        backward = [nums[(minIndex + 1 + i) % n] for i in range(n)][::-1]
        return max(self.computeScore(forward, k), self.computeScore(backward, k))

    def computeScore(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [[-math.inf] * (n + 1) for _ in range(k + 1)]

        mn = math.inf
        mx = -math.inf

        for idx in range(n):
            mn = min(mn, arr[idx])
            mx = max(mx, arr[idx])
            dp[1][idx + 1] = mx - mn

        result = dp[1][n]

        for group in range(2, k + 1):
            bestMinus = -math.inf
            bestPlus = -math.inf
            for idx in range(group - 1, n):
                bestMinus = max(bestMinus, dp[group - 1][idx] - arr[idx])
                bestPlus = max(bestPlus, dp[group - 1][idx] + arr[idx])
                dp[group][idx + 1] = max(dp[group][idx], bestMinus + arr[idx], bestPlus - arr[idx])
            result = max(result, dp[group][n])

        return int(result)
