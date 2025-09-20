from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
from typing import List

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.destMap = defaultdict(deque)
        self.packetQueue = deque()
        self.packetSet = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packetSet:
            return False
        self.packetQueue.append(packet)
        self.destMap[destination].append(timestamp)
        self.packetSet.add(packet)
        if len(self.packetQueue) > self.memoryLimit:
            oldPacket = self.packetQueue.popleft()
            self.destMap[oldPacket[1]].popleft()
            self.packetSet.remove(oldPacket)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packetQueue:
            return []
        packet = self.packetQueue.popleft()
        self.destMap[packet[1]].popleft()
        self.packetSet.remove(packet)
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.destMap[destination]
        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)
        return right - left
