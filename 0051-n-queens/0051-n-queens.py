def isSafe(row, col, board, n):
    tempRow = row
    tempCol = col

    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1

    row = tempRow
    col = tempCol

    while col >= 0:
        if board[row][col] == "Q":
            return False
        col -= 1

    col = tempCol

    while row < n and col >= 0:
        if board[row][col] == "Q":
            return False
        row += 1
        col -= 1

    return True

def solveNQueensHelper(col, solutions, board, n):
    if col == n:
        solutions.append(board[:])
        return

    for row in range(n):
        if isSafe(row, col, board, n):
            board[row] = board[row][:col] + "Q" + board[row][col + 1:]
            solveNQueensHelper(col + 1, solutions, board, n)
            board[row] = board[row][:col] + "." + board[row][col + 1:]

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        solutions = []
        board = ['.' * n for _ in range(n)]
        solveNQueensHelper(0, solutions, board, n)
        return solutions
