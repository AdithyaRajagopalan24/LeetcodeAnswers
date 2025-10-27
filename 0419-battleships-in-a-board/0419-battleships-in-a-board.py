from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        totalShips = 0

        for rowIndex, row in enumerate(board):
            for colIndex, cell in enumerate(row):
                if cell == "X":
                    isTopClear = rowIndex == 0 or board[rowIndex - 1][colIndex] == "."
                    isLeftClear = colIndex == 0 or board[rowIndex][colIndex - 1] == "."
                    
                    if isTopClear and isLeftClear:
                        totalShips += 1

        return totalShips
