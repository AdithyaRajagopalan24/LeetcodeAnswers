class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = deque()

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while fresh and rotten:
            level = len(rotten)

            while level:
                x, y = rotten.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (nx, ny) not in fresh:
                        continue

                    fresh.remove((nx, ny))
                    rotten.append((nx, ny))

                level -= 1

            minutes += 1

        if fresh:
            return -1
        return minutes