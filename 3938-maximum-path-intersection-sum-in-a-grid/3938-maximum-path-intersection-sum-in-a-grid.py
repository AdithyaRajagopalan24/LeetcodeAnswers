from math import inf

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        answer = -inf

        for row in range(rows):
            down = -inf
            up = grid[row][0]

            for col in range(1, cols):
                up += grid[row][col]
                down = max(down, up)

                if up < grid[row][col]:
                    up = grid[row][col]

            answer = max(answer, down)

        for col in range(cols):
            down = -inf
            up = grid[0][col]

            for row in range(1, rows):
                up += grid[row][col]
                down = max(down, up)

                if up < grid[row][col]:
                    up = grid[row][col]

            answer = max(answer, down)

        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                answer = max(answer, grid[row][col])

        return answer