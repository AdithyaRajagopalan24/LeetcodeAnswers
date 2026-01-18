class Solution:
    def largestMagicSquare(self, grid):
        rowCount, colCount = len(grid), len(grid[0])

        rowPrefixSum = [[0] * (colCount + 1) for _ in range(rowCount)]
        colPrefixSum = [[0] * colCount for _ in range(rowCount + 1)]

        for rowIndex in range(rowCount):
            for colIndex in range(colCount):
                rowPrefixSum[rowIndex][colIndex + 1] = rowPrefixSum[rowIndex][colIndex] + grid[rowIndex][colIndex]

        for colIndex in range(colCount):
            for rowIndex in range(rowCount):
                colPrefixSum[rowIndex + 1][colIndex] = colPrefixSum[rowIndex][colIndex] + grid[rowIndex][colIndex]

        maxSize = 1

        for startRow in range(rowCount):
            for startCol in range(colCount):
                maxPossibleSize = min(rowCount - startRow, colCount - startCol)
                for size in range(maxPossibleSize, maxSize, -1):
                    if self.isMagicSquare(grid, rowPrefixSum, colPrefixSum, startRow, startCol, size):
                        maxSize = size
                        break

        return maxSize

    def isMagicSquare(self, grid, rowPrefixSum, colPrefixSum, startRow, startCol, size):
        targetSum = rowPrefixSum[startRow][startCol + size] - rowPrefixSum[startRow][startCol]

        for rowOffset in range(size):
            if rowPrefixSum[startRow + rowOffset][startCol + size] - rowPrefixSum[startRow + rowOffset][startCol] != targetSum:
                return False

        for colOffset in range(size):
            if colPrefixSum[startRow + size][startCol + colOffset] - colPrefixSum[startRow][startCol + colOffset] != targetSum:
                return False

        mainDiagonalSum = 0
        antiDiagonalSum = 0

        for offset in range(size):
            mainDiagonalSum += grid[startRow + offset][startCol + offset]
            antiDiagonalSum += grid[startRow + size - 1 - offset][startCol + offset]

        return mainDiagonalSum == targetSum and antiDiagonalSum == targetSum
