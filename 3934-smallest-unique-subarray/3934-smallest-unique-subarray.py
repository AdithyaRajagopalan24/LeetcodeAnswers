from collections import Counter
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mod1, mod2 = 10**9 + 7, 10**9 + 9
        base1, base2 = 100237, 199777

        def hasUnique(length: int) -> bool:
            if length == 0:
                return False

            basePow1 = pow(base1, length, mod1)
            basePow2 = pow(base2, length, mod2)
            hash1 = hash2 = 0
            for i in range(length):
                hash1 = (hash1 * base1 + nums[i]) % mod1
                hash2 = (hash2 * base2 + nums[i]) % mod2
            hashCounts = Counter([(hash1, hash2)])

            for i in range(length, n):
                hash1 = (hash1 * base1 + nums[i] - nums[i - length] * basePow1) % mod1
                hash2 = (hash2 * base2 + nums[i] - nums[i - length] * basePow2) % mod2
                hashCounts[(hash1, hash2)] += 1

            return 1 in hashCounts.values()

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if hasUnique(mid):
                right = mid
            else:
                left = mid + 1
        return left