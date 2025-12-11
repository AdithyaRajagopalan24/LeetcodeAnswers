class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        row_ranges = {}
        col_ranges = {}
        
        for bx, by in buildings:
            if bx not in row_ranges:
                row_ranges[bx] = [by, by]
            else:
                row_ranges[bx][0] = min(row_ranges[bx][0], by)
                row_ranges[bx][1] = max(row_ranges[bx][1], by)
            
            if by not in col_ranges:
                col_ranges[by] = [bx, bx]
            else:
                col_ranges[by][0] = min(col_ranges[by][0], bx)
                col_ranges[by][1] = max(col_ranges[by][1], bx)
        
        covered_count = 0
        for bx, by in buildings:
            row_min, row_max = row_ranges[bx]
            col_min, col_max = col_ranges[by]
            
            if row_min < by < row_max and col_min < bx < col_max:
                covered_count += 1
        
        return covered_count
