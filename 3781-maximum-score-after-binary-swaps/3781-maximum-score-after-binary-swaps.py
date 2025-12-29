class Solution:
    def maximumScore(self, numbers: List[int], operations: str) -> int:
        maxHeap = []
        totalScore = 0
        for index, number in enumerate(numbers):
            heapq.heappush(maxHeap, -number)
            if operations[index] == '1':
                totalScore -= heapq.heappop(maxHeap)
        return totalScore
