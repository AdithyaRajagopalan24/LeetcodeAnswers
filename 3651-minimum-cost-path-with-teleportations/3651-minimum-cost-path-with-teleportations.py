class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        rowCount, colCount = len(grid), len(grid[0])
        maxValue = max(max(row) for row in grid)

        def runDp(dpTable: list[list[int]], bestTeleport: list[int]) -> list[list[int]]:
            for row in reversed(range(rowCount)):
                for col in reversed(range(colCount)):
                    cost = math.inf if (row, col) != (rowCount - 1, colCount - 1) else 0
                    if row + 1 < rowCount:
                        cost = min(cost, dpTable[row + 1][col] + grid[row + 1][col])
                    if col + 1 < colCount:
                        cost = min(cost, dpTable[row][col + 1] + grid[row][col + 1])
                    dpTable[row][col] = min(cost, bestTeleport[grid[row][col]])
            return dpTable

        def buildBestTeleport(dpTable: list[list[int]]) -> list[int]:
            teleportCost = [math.inf] * (maxValue + 1)

            for row, col in product(range(rowCount), range(colCount)):
                value = grid[row][col]
                teleportCost[value] = min(teleportCost[value], dpTable[row][col])

            for value in range(maxValue + 1):
                if value > 0:
                    teleportCost[value] = min(teleportCost[value], teleportCost[value - 1])

            return teleportCost

        bestTeleport = [math.inf] * (maxValue + 1)
        dpTable = [[math.inf] * colCount for _ in range(rowCount)]
        dpTable[-1][-1] = 0

        for _ in range(k + 1):
            dpTable = runDp(dpTable, bestTeleport)
            bestTeleport = buildBestTeleport(dpTable)

        return dpTable[0][0]
