from bisect import bisect_right
from sortedcontainers import SortedList
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = [-1] * len(rains)
        lakeFull = {}
        dryDays = SortedList()

        for day, lake in enumerate(rains):
            if lake == 0:
                dryDays.add(day)
                result[day] = 1
            elif lake in lakeFull:
                dryIndex = dryDays.bisect_right(lakeFull[lake])
                if dryIndex == len(dryDays):
                    return []
                result[dryDays[dryIndex]] = lake
                dryDays.pop(dryIndex)
                lakeFull[lake] = day
            else:
                lakeFull[lake] = day

        return result
