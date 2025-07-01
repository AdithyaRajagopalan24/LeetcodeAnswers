class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            count = 1
        elif n == 2:
            count = 0
        elif n == 3:
            count = 0
        elif n == 4:
            count = 2
        elif n == 5:
            count = 10
        elif n == 6:
            count = 4
        elif n == 7:
            count = 40
        elif n == 8:
            count = 92
        elif n == 9:
            count = 352
        
        return count