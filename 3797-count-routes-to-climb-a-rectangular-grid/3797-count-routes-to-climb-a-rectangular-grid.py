class Solution:
    def numberOfRoutes(self, grid: List[str], maxDist: int) -> int:
        mod = 1000000007
        rows = len(grid)
        cols = len(grid[0])

        prevRoutes = [0] * cols

        for col in range(cols):
            if grid[0][col] == '#':
                continue
            safeRoutes = 0
            for j in range(col + 1, min(col + maxDist, cols - 1) + 1):
                if grid[0][j] != '#':
                    safeRoutes += 1
            for j in range(max(0, col - maxDist), col):
                if grid[0][j] != '#':
                    safeRoutes += 1
            prevRoutes[col] = safeRoutes + 1

        maxColDist = 0
        for col in range(cols):
            distSquared = 1 + col * col
            if distSquared <= maxDist * maxDist:
                maxColDist = col
            else:
                break

        for row in range(1, rows):
            for col in range(1, cols):
                prevRoutes[col] = (prevRoutes[col] + prevRoutes[col - 1]) % mod

            prefRoutes = [0] * cols
            for col in range(cols):
                if grid[row][col] == '#':
                    continue
                lastCol = min(col + maxColDist, cols - 1)
                prefRoutes[col] = prevRoutes[lastCol]
                if col > maxColDist:
                    prefRoutes[col] = (prefRoutes[col] - prevRoutes[col - maxColDist - 1]) % mod

            for col in range(1, cols):
                prefRoutes[col] = (prefRoutes[col] + prefRoutes[col - 1]) % mod

            curRoutes = [0] * cols
            for col in range(cols):
                if grid[row][col] == '#':
                    continue
                curRoutes[col] = prefRoutes[min(col + maxDist, cols - 1)]
                if col > maxDist:
                    curRoutes[col] = (curRoutes[col] - prefRoutes[col - maxDist - 1]) % mod

            prevRoutes = curRoutes

        return sum(prevRoutes) % mod
