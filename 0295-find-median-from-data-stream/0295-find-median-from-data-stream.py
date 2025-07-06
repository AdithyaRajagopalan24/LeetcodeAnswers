from heapq import heappush, heappop, heappushpop

class MedianFinder(object):
    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num):
        if len(self.maxheap) == len(self.minheap):
            heappush(self.minheap, -heappushpop(self.maxheap, -num))
        else:
            heappush(self.maxheap, -heappushpop(self.minheap, num))

    def findMedian(self):
        if len(self.maxheap) == len(self.minheap):
            return float(self.minheap[0] - self.maxheap[0]) / 2.0
        else:
            return float(self.minheap[0])