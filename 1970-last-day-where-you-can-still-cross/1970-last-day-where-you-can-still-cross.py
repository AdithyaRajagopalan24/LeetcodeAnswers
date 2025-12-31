class Solution:
    def latestDayToCross(self, n: int, m: int, cells: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def canCross(day: int) -> bool:
            visited = [[False] * m for _ in range(n)]
            grid = [[0] * m for _ in range(n)]
            for i in range(day):
                x, y = cells[i]
                grid[x - 1][y - 1] = 1

            def dfs(row, col):
                if row == n - 1:
                    return True
                visited[row][col] = True
                for dx, dy in directions:
                    newRow, newCol = row + dx, col + dy
                    if 0 <= newRow < n and 0 <= newCol < m:
                        if not visited[newRow][newCol] and grid[newRow][newCol] == 0:
                            if dfs(newRow, newCol):
                                return True
                return False

            for col in range(m):
                if grid[0][col] == 0 and not visited[0][col]:
                    if dfs(0, col):
                        return True
            return False

        low, high = 0, len(cells)
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if canCross(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
