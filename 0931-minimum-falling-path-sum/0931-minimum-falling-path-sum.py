class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        size = len(grid)
        dpTable = [[0] * size for _ in range(size)]
        dpTable[0] = grid[0][:]

        for row in range(1, size):
            for col in range(size):
                if col == 0:
                    dpTable[row][col] = min(
                        dpTable[row - 1][col],
                        dpTable[row - 1][col + 1]
                    ) + grid[row][col]
                elif col == size - 1:
                    dpTable[row][col] = min(
                        dpTable[row - 1][col - 1],
                        dpTable[row - 1][col]
                    ) + grid[row][col]
                else:
                    dpTable[row][col] = min(
                        dpTable[row - 1][col - 1],
                        dpTable[row - 1][col],
                        dpTable[row - 1][col + 1]
                    ) + grid[row][col]

        return min(dpTable[-1])