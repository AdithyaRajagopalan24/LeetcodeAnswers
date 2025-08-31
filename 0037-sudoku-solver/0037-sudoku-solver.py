from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_mask = [0] * 9
        col_mask = [0] * 9
        box_mask = [0] * 9
        empties = []

        def bit(d): return 1 << d

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empties.append((r, c))
                else:
                    d = int(board[r][c]) - 1
                    row_mask[r] |= bit(d)
                    col_mask[c] |= bit(d)
                    box_mask[(r // 3) * 3 + c // 3] |= bit(d)

        def backtrack():
            if not empties:
                return True
            empties.sort(key=lambda x: bin(~(row_mask[x[0]] | col_mask[x[1]] | box_mask[(x[0]//3)*3+x[1]//3]) & 0x1FF).count("1"))
            r, c = empties.pop(0)
            b = (r // 3) * 3 + c // 3
            used = row_mask[r] | col_mask[c] | box_mask[b]
            for d in range(9):
                if not (used & bit(d)):
                    board[r][c] = str(d + 1)
                    row_mask[r] |= bit(d)
                    col_mask[c] |= bit(d)
                    box_mask[b] |= bit(d)
                    if backtrack():
                        return True
                    board[r][c] = "."
                    row_mask[r] ^= bit(d)
                    col_mask[c] ^= bit(d)
                    box_mask[b] ^= bit(d)
            empties.insert(0, (r, c))
            return False

        backtrack()
