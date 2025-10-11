from bisect import bisect_right

class Solution:
    def maximumTotalDamage(self, powerList: list[int]) -> int:
        freqMap = {}
        for p in powerList:
            freqMap[p] = freqMap.get(p, 0) + 1
        valueList = sorted(freqMap.keys())
        n = len(valueList)
        dpList = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            totalDamage = valueList[i] * freqMap[valueList[i]]
            nextIndex = bisect_right(valueList, valueList[i] + 2)
            dpList[i] = max(dpList[i + 1], totalDamage + dpList[nextIndex])
        return dpList[0]
