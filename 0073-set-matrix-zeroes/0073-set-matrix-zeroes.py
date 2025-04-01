class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for i in set(rows):
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in set(cols):
            for j in range(len(matrix)):
                matrix[j][i] = 0