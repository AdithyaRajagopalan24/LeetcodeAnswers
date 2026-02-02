class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        window = Window(k - 1)

        for i in range(1, dist + 2):
            window.add(nums[i])

        minCost = window.cost
        for i in range(2, n - dist):
            window.remove(nums[i - 1])
            window.add(nums[i + dist])
            minCost = min(minCost, window.cost)

        return nums[0] + minCost


class Window:
    def __init__(self, k: int):
        self.k = k
        self.minHeap = []
        self.maxHeap = []
        self.cost = 0
        self.delMin = defaultdict(int)
        self.delMax = defaultdict(int)
        self.minSize = 0
        self.maxSize = 0

    def pruneMax(self):
        while self.maxHeap:
            val = -self.maxHeap[0]
            if self.delMax[val] == 0:
                break
            heapq.heappop(self.maxHeap)
            self.delMax[val] -= 1

    def pruneMin(self):
        while self.minHeap:
            val = self.minHeap[0]
            if self.delMin[val] == 0:
                break
            heapq.heappop(self.minHeap)
            self.delMin[val] -= 1

    def rebalance(self):
        target = min(self.k, self.maxSize + self.minSize)

        if self.maxSize > target:
            self.pruneMax()
        while self.maxSize > target:
            val = -heapq.heappop(self.maxHeap)
            self.maxSize -= 1
            self.cost -= val
            heapq.heappush(self.minHeap, val)
            self.minSize += 1
            self.pruneMax()

        if self.maxSize < target:
            self.pruneMin()
        while self.maxSize < target:
            val = heapq.heappop(self.minHeap)
            self.minSize -= 1
            heapq.heappush(self.maxHeap, -val)
            self.maxSize += 1
            self.cost += val
            self.pruneMin()

    def add(self, value: int):
        if not self.maxHeap or value <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -value)
            self.maxSize += 1
            self.cost += value
        else:
            heapq.heappush(self.minHeap, value)
            self.minSize += 1
        self.rebalance()

    def remove(self, value: int):
        if value <= -self.maxHeap[0]:
            self.delMax[value] += 1
            self.maxSize -= 1
            self.cost -= value
        else:
            self.delMin[value] += 1
            self.minSize -= 1
        self.rebalance()
        