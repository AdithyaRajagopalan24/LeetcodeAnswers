class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        dp = [[None for _ in range(n)] for _ in range(m)]

        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]
            length = 1
            for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[r][c]:
                    length = max(length, dfs(x, y) + 1)
            dp[r][c] = length
            return length

        for r in range(m):
            for c in range(n):
                dfs(r, c)

        return max(max(row) for row in dp)
