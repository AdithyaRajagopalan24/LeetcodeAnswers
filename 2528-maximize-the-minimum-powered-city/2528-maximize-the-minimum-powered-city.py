from typing import List
import bisect

class Solution:
    def maxPower(self, stations: List[int], radius: int, extraStations: int) -> int:
        n = len(stations)
        prefixDiff = [0] * (n + 1)
        for i in range(n):
            left = max(0, i - radius)
            right = min(n, i + radius + 1)
            prefixDiff[left] += stations[i]
            prefixDiff[right] -= stations[i]

        def canReach(target: int) -> bool:
            diffCopy = prefixDiff.copy()
            current = 0
            remaining = extraStations
            for i in range(n):
                current += diffCopy[i]
                if current < target:
                    needed = target - current
                    if remaining < needed:
                        return False
                    remaining -= needed
                    end = min(n, i + 2 * radius + 1)
                    diffCopy[end] -= needed
                    current += needed
            return True

        low, high = min(stations), sum(stations) + extraStations
        powerRange = range(low, high + 1)
        index = bisect.bisect_left(powerRange, 1, key=lambda val: not canReach(val)) - 1
        return powerRange[index]
