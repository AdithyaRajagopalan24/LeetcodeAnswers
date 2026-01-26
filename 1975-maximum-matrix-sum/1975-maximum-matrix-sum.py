class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalSum = 0
        negativeCount = 0
        minAbsValue = float('inf')

        for row in matrix:
            for value in row:
                absValue = abs(value)
                totalSum += absValue
                if value < 0:
                    negativeCount += 1
                if absValue < minAbsValue:
                    minAbsValue = absValue

        if negativeCount % 2 == 1:
            totalSum -= 2 * minAbsValue

        return totalSum

