import heapq

class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cost = [[float('inf')] * n for _ in range(m)]
        pq = []
        heapq.heappush(pq, (0, 0, 0))
        cost[0][0] = 0

        while pq:
            currCost, i, j = heapq.heappop(pq)
            if i == m - 1 and j == n - 1:
                return currCost
            for dir, (di, dj) in enumerate(directions):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    newCost = currCost if grid[i][j] == dir + 1 else currCost + 1
                    if newCost < cost[ni][nj]:
                        cost[ni][nj] = newCost
                        heapq.heappush(pq, (newCost, ni, nj))
        return cost[m - 1][n - 1]
