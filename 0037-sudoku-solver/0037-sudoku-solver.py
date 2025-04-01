class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [[set() for _ in range(3)] for _ in range(3)]
        empty_cells = []
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value == ".":
                    empty_cells.append((i, j))
                else:
                    rows[i].add(value)
                    cols[j].add(value)
                    grids[i//3][j//3].add(value)                     
        empty_cells = [
            (9 - len(rows[i] | cols[j] | grids[i//3][j//3]), i, j)
            for i, j in empty_cells
        ]
        heapq.heapify(empty_cells)
        def fill_board():
            if not empty_cells: 
                return True
            _, i, j = heapq.heappop(empty_cells)
            row = rows[i]
            col = cols[j]
            grid = grids[i//3][j//3]
            potential_nums = 0  
            for value in '123456789':
                if (value in row or value in col or value in grid): 
                    continue
                board[i][j] = value
                row.add(value)
                col.add(value)
                grid.add(value)

                if fill_board():
                    return True
                row.remove(value)
                col.remove(value)
                grid.remove(value)
                potential_nums += 1
            heapq.heappush(empty_cells, (potential_nums, i, j))
            return False
            
        fill_board()
