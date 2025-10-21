from collections import defaultdict, deque
from typing import List

class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], window: int, maxCount: int) -> int:
        typeQueue = defaultdict(deque)
        discardCount = 0

        for day, arrivalType in enumerate(arrivals, 1):
            queue = typeQueue[arrivalType]
            leftBound = day - window + 1

            while queue and queue[0] < leftBound:
                queue.popleft()

            if len(queue) >= maxCount:
                discardCount += 1
            else:
                queue.append(day)

        return discardCount
