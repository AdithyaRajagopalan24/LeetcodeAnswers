class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def collect_fish(i, j):
            num_fish = grid[i][j] 
            grid[i][j] = 0

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != 0: 
                    num_fish += collect_fish(ni, nj)

            return num_fish

        m = len(grid)
        n = len(grid[0])
        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                max_fish = max(max_fish, collect_fish(i, j))

        return max_fish