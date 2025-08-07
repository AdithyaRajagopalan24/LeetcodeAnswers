class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        size = len(fruits)
        mainDiagonalSum = sum(fruits[i][i] for i in range(size))

        for row in range(size - 2):
            fruits[row][size - 2 - row] = 0
            fruits[row][size - 3 - row] = 0
        fruits[size - 2][0] = 0

        for row in range(1, size - 1):
            for col in range(max(row + 1, size - row - 1), size - 1):
                fruits[row][col] += max(
                    fruits[row - 1][col - 1],
                    fruits[row - 1][col],
                    fruits[row - 1][col + 1]
                )
            fruits[row][-1] += max(fruits[row - 1][-2], fruits[row - 1][-1])

        for col in range(1, size - 1):
            for row in range(max(col + 1, size - col - 1), size - 1):
                fruits[row][col] += max(
                    fruits[row - 1][col - 1],
                    fruits[row][col - 1],
                    fruits[row + 1][col - 1]
                )
            fruits[-1][col] += max(fruits[-2][col - 1], fruits[-1][col - 1])

        return mainDiagonalSum + fruits[size - 2][size - 1] + fruits[size - 1][size - 2]
