class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)] 
        inBounds = lambda r, c: 0 <= r < rows and 0 <= c < cols
        maxLen = 0

        dpZero = [[[0] * cols for _ in range(rows)] for _ in range(4)] 
        dpTwo = [[[0] * cols for _ in range(rows)] for _ in range(4)] 
        for d, (dr, dc) in enumerate(directions):
            rowOrder = range(rows - 1, -1, -1) if dr >= 0 else range(rows)
            colOrder = range(cols - 1, -1, -1) if dc >= 0 else range(cols)
            for r in rowOrder:
                for c in colOrder:
                    nr, nc = r + dr, c + dc
                    if grid[r][c] == 0:
                        dpZero[d][r][c] = 1 + (dpTwo[d][nr][nc] if inBounds(nr, nc) else 0)
                    if grid[r][c] == 2:
                        dpTwo[d][r][c] = 1 + (dpZero[d][nr][nc] if inBounds(nr, nc) else 0)

        for d, (dr, dc) in enumerate(directions):
            turnDir = (d + 1) % 4  
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] != 1:
                        continue
                    cr, cc, need, length = r, c, 1, 0
                    while inBounds(cr, cc) and grid[cr][cc] == need:
                        length += 1
                        maxLen = max(maxLen, length)
                        tr, tc = cr + directions[turnDir][0], cc + directions[turnDir][1]
                        if inBounds(tr, tc):
                            maxLen = max(maxLen, length + (dpTwo[turnDir][tr][tc] if length & 1 else dpZero[turnDir][tr][tc]))
                        cr, cc = cr + dr, cc + dc
                        need = 2 if need == 1 else (0 if need == 2 else 2)

        return maxLen
