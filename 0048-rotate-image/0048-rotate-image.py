class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        def reverse(row):
            left = 0
            right = len(row) - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(rows):
            reverse(matrix[i])