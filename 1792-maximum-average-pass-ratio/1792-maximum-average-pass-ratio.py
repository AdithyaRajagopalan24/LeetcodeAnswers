from heapq import heapify, heappush, heappop

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def marginalGain(passCount: int, totalCount: int) -> float:
            return (passCount + 1) / (totalCount + 1) - passCount / totalCount

        gainHeap = [(-marginalGain(passCount, totalCount), passCount, totalCount) for passCount, totalCount in classes]
        heapify(gainHeap)

        for _ in range(extraStudents):
            _, passCount, totalCount = heappop(gainHeap)
            passCount += 1
            totalCount += 1
            heappush(gainHeap, (-marginalGain(passCount, totalCount), passCount, totalCount))

        classCount = len(classes)
        ratioSum = sum(passCount / totalCount for _, passCount, totalCount in gainHeap)
        return ratioSum / classCount
