from heapq import heappop, heappush
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        numRows, numCols = len(moveTime), len(moveTime[0])
        def isOutOfBounds(x, y):
            return x < 0 or x >= numRows or y < 0 or y >= numCols
        def toIndex(x, y):
            return x * numCols + y

        totalCells = numRows * numCols
        minTime = [2**31] * totalCells
        priorityQueue = [0]
        minTime[0] = 0
        while priorityQueue:
            packedState = heappop(priorityQueue)
            currentTime = packedState >> 32
            cellIndex = packedState & ((1 << 30) - 1)
            row, col = divmod(cellIndex, numCols)
            if row == numRows - 1 and col == numCols - 1:
                return currentTim
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newRow, newCol = row + dx, col + dy
                if isOutOfBounds(newRow, newCol):
                    continue
                nextTime = max(currentTime, moveTime[newRow][newCol]) + 1
                newIndex = toIndex(newRow, newCol)
                if nextTime < minTime[newIndex]:
                    minTime[newIndex] = nextTime
                    heappush(priorityQueue, (nextTime << 32) + newIndex)
        return -1
