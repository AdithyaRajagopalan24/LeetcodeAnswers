import heapq

class Solution:
    def swimInWater(self, grid):
        n, seen, pq = len(grid), {(0, 0)}, [(grid[0][0], 0, 0)]
        while pq:
            t, r, c = heapq.heappop(pq)
            if (r, c) == (n - 1, n - 1): return t
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    heapq.heappush(pq, (max(t, grid[nr][nc]), nr, nc))
