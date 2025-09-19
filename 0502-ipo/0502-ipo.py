import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, initialCapital: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projectList = [(capital[i], profits[i]) for i in range(n)]
        projectList.sort()
        maxHeap = []
        idx = 0
        currentCapital = initialCapital
        while k > 0:
            while idx < n and projectList[idx][0] <= currentCapital:
                heapq.heappush(maxHeap, -projectList[idx][1])
                idx += 1
            if not maxHeap:
                break
            currentCapital += -heapq.heappop(maxHeap)
            k -= 1
        return currentCapital