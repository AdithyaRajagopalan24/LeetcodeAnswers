class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        straightenedGrid = [n for row in grid for n in row]

        for num in straightenedGrid:
            if (num - straightenedGrid[0]) % x != 0:
                return -1
        
        straightenedGrid.sort()
        median = straightenedGrid[len(straightenedGrid)//2]

        op = sum(abs(n-median)//x for n in straightenedGrid)
        return op