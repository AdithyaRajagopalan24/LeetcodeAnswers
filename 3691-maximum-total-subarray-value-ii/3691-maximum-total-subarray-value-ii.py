import heapq
from typing import List

class SparseTable:
    def __init__(self, arr: List[int]):
        n = len(arr)
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1
        maxLog = self.log[n] + 1

        self.minTable = [[0] * maxLog for _ in range(n)]
        self.maxTable = [[0] * maxLog for _ in range(n)]

        for i in range(n):
            self.minTable[i][0] = self.maxTable[i][0] = arr[i]

        j = 1
        while (1 << j) <= n:
            for i in range(n - (1 << j) + 1):
                self.minTable[i][j] = min(
                    self.minTable[i][j - 1],
                    self.minTable[i + (1 << (j - 1))][j - 1]
                )
                self.maxTable[i][j] = max(
                    self.maxTable[i][j - 1],
                    self.maxTable[i + (1 << (j - 1))][j - 1]
                )
            j += 1

    def queryMin(self, left: int, right: int) -> int:
        j = self.log[right - left + 1]
        return min(self.minTable[left][j], self.minTable[right - (1 << j) + 1][j])

    def queryMax(self, left: int, right: int) -> int:
        j = self.log[right - left + 1]
        return max(self.maxTable[left][j], self.maxTable[right - (1 << j) + 1][j])


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        table = SparseTable(nums)
        total = 0

        heap = [
            (-(table.queryMax(0, i) - table.queryMin(0, i)), 0, i)
            for i in range(n)
        ]
        heapq.heapify(heap)

        for _ in range(k):
            value, left, right = heapq.heappop(heap)
            total -= value
            if left + 1 <= right:
                newValue = table.queryMax(left + 1, right) - table.queryMin(left + 1, right)
                heapq.heappush(heap, (-newValue, left + 1, right))

        return total
