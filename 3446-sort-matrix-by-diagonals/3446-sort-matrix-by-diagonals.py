class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for d in range(n - 2, -1, -1):
            diag = sorted(grid[i][i + d] for i in range(n - d))
            for i, v in enumerate(diag):
                grid[i][i + d] = v
        for d in range(n - 1):
            diag = sorted((grid[j + d][j] for j in range(n - d)), reverse=True)
            for j, v in enumerate(diag):
                grid[j + d][j] = v
        return grid
