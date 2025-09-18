import heapq

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.pq = []
        self.taskStore = {}
        for userId, taskId, priority in tasks:
            self.taskStore[taskId] = [userId, taskId, priority]
            heapq.heappush(self.pq, (-priority, -taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskStore[taskId] = [userId, taskId, priority]
        heapq.heappush(self.pq, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _, _ = self.taskStore[taskId]
        self.taskStore[taskId] = [userId, taskId, newPriority]
        heapq.heappush(self.pq, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.taskStore[taskId]

    def execTop(self) -> int:
        if not self.pq or not self.taskStore:
            return -1
        priority, taskId = heapq.heappop(self.pq)
        while -taskId not in self.taskStore or -priority != self.taskStore[-taskId][2]:
            if not self.pq:
                return -1
            priority, taskId = heapq.heappop(self.pq)
        userId = self.taskStore[-taskId][0]
        del self.taskStore[-taskId]
        return userId
