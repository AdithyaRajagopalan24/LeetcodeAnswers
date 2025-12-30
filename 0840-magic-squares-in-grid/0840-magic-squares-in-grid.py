class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        magicSquare = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
        validSquares = []
        validPatterns = set()
        current = magicSquare
        count = 0
        if rows < 3 or cols < 3:
            return 0

        def rotate(square):
            return [[square[2][0], square[1][0], square[0][0]],
                    [square[2][1], square[1][1], square[0][1]],
                    [square[2][2], square[1][2], square[0][2]]]
    
        for _ in range(4):
            validSquares.append(current)
            current = rotate(current)
            
        current = [[magicSquare[j][i] for j in range(3)] for i in range(3)]
        for _ in range(4):
            validSquares.append(current)
            current = rotate(current)
        
        for square in validSquares:
            flat = tuple(num for row in square for num in row)
            validPatterns.add(flat)

        for r in range(rows - 2):
            for c in range(cols - 2):
                if grid[r+1][c+1] != 5:
                    continue               
                subgrid = (
                    grid[r][c],   grid[r][c+1],   grid[r][c+2],
                    grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                    grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]
                )      
                if subgrid in validPatterns:
                    count += 1
                    
        return count
