class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows*cols-1

        while start <= end:
            mid = (start+end)//2
            row = mid//cols
            col = mid%cols
            if matrix[row][col] < target:
                start = mid + 1
            elif matrix[row][col] > target:
                end = mid - 1
            elif matrix[row][col] == target:
                return True
        return False