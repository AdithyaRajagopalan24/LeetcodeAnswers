class Solution:
    def maxSideLength(self, matrix: List[List[int]], threshold: int) -> int:
        rowCount, colCount = len(matrix), len(matrix[0])
        prefixSum = [[0] * (colCount + 1) for _ in range(rowCount + 1)]

        for row in range(rowCount):
            for col in range(colCount):
                prefixSum[row + 1][col + 1] = matrix[row][col] + prefixSum[row][col + 1] + prefixSum[row + 1][col] - prefixSum[row][col]

        def isValidSquare(sideLength: int) -> bool:
            for row in range(sideLength, rowCount + 1):
                for col in range(sideLength, colCount + 1):
                    squareSum = prefixSum[row][col] - prefixSum[row - sideLength][col] - prefixSum[row][col - sideLength] + prefixSum[row - sideLength][col - sideLength]
                    if squareSum <= threshold:
                        return True
            return False

        left, right, bestSideLength = 0, min(rowCount, colCount), 0

        while left <= right:
            mid = (left + right) // 2
            if isValidSquare(mid):
                bestSideLength, left = mid, mid + 1
            else:
                right = mid - 1

        return bestSideLength
