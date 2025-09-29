from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        minEndL = min(s + d for s, d in zip(landStartTime, landDuration))
        minEndW = min(s + d for s, d in zip(waterStartTime, waterDuration))
        resL = min(max(minEndW, s) + d for s, d in zip(landStartTime, landDuration))
        resW = min(max(minEndL, s) + d for s, d in zip(waterStartTime, waterDuration))
        return min(resL, resW)
