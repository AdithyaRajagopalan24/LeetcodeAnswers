class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        a = sum(grid[0])
        b = 0
        res = float('inf')
        for i in range(len(grid[0])):
            a -= grid[0][i]
            res = min(res, max(a, b))
            b += grid[1][i]
        return res