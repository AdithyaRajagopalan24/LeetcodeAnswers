class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        rc = [0] * rows
        cc = [0] * columns
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]:
                    rc[i] += 1
                    cc[j] += 1
        ans = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] and (rc[i] > 1 or cc[j] > 1):
                    ans += 1
        return ans
