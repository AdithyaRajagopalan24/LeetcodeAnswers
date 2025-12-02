import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        maxHeap = [-x for x in target]
        heapq.heapify(maxHeap)
        total = sum(target)
        while True:
            largest = -heapq.heappop(maxHeap)
            rest = total - largest
            if largest == 1 or rest == 1:
                return True
            if rest == 0 or largest < rest or largest % rest == 0:
                return False
            prev = largest % rest
            total = rest + prev
            heapq.heappush(maxHeap, -prev)
 