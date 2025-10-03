import heapq

class Cell:
    def __init__(self, height, row, col):
        self.height = height
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.height < other.height

class Solution:
    def check(self, x, y, n, m):
        return 0 <= x < n and 0 <= y < m

    def trapRainWater(self, heightMap):
        n = len(heightMap)
        m = len(heightMap[0])
        trappedWater = 0
        priorityQueue = []
        visited = [[False] * m for _ in range(n)]

        for i in range(n):
            heapq.heappush(priorityQueue, Cell(heightMap[i][0], i, 0))
            heapq.heappush(priorityQueue, Cell(heightMap[i][m - 1], i, m - 1))
            visited[i][0] = visited[i][m - 1] = True

        for j in range(m):
            heapq.heappush(priorityQueue, Cell(heightMap[0][j], 0, j))
            heapq.heappush(priorityQueue, Cell(heightMap[n - 1][j], n - 1, j))
            visited[0][j] = visited[n - 1][j] = True

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        while priorityQueue:
            cell = heapq.heappop(priorityQueue)
            for dx, dy in directions:
                x, y = cell.row + dx, cell.col + dy
                if self.check(x, y, n, m) and not visited[x][y]:
                    if heightMap[x][y] < cell.height:
                        trappedWater += cell.height - heightMap[x][y]
                        heapq.heappush(priorityQueue, Cell(cell.height, x, y))
                    else:
                        heapq.heappush(priorityQueue, Cell(heightMap[x][y], x, y))
                    visited[x][y] = True

        return trappedWater
