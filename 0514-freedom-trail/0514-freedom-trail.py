from functools import lru_cache
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @lru_cache(None)
        def dfs(keyIdx, ringPos):
            if keyIdx == len(key):
                return 0
            minSteps = float('inf')
            for targetPos in charPositions[key[keyIdx]]:
                dist = abs(ringPos - targetPos)
                rotateSteps = min(dist, ringLen - dist) + 1
                minSteps = min(minSteps, rotateSteps + dfs(keyIdx + 1, targetPos))
            return minSteps

        ringLen = len(ring)
        charPositions = defaultdict(list)
        for idx, char in enumerate(ring):
            charPositions[char].append(idx)

        return dfs(0, 0)
