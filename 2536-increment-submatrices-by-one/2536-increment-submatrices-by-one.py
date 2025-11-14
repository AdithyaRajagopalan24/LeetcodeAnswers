class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diffMat = [[0] * n for _ in range(n)]
        for top, left, bottom, right in queries:
            diffMat[top][left] += 1
            if bottom + 1 < n: diffMat[bottom + 1][left] -= 1
            if right + 1 < n: diffMat[top][right + 1] -= 1
            if bottom + 1 < n and right + 1 < n: diffMat[bottom + 1][right + 1] += 1
        for i in range(n):
            for j in range(1, n):
                diffMat[i][j] += diffMat[i][j - 1]
        for i in range(1, n):
            for j in range(n):
                diffMat[i][j] += diffMat[i - 1][j]
        return diffMat
