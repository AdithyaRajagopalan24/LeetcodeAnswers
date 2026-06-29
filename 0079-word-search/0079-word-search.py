class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        if len(word) > rows * cols:
            return False

        board_count = Counter(sum(board, []))
        word_count = Counter(word)

        for ch, needed in word_count.items():
            if board_count[ch] < needed:
                return False

        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        visited = set()

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx] or (r, c) in visited:
                return False

            visited.add((r, c))

            result = dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1)

            visited.remove((r, c))
            return result

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False