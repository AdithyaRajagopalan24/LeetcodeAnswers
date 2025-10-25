class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        return self.dfs(board, "".join(sorted(hand)), {})

    def removeBalls(self, board: str, idx: int) -> str:
        if idx < 0:
            return board

        left = right = idx
        while left > 0 and board[left] == board[left - 1]:
            left -= 1
        while right < len(board) - 1 and board[right] == board[right + 1]:
            right += 1

        if right - left + 1 >= 3:
            return self.removeBalls(board[:left] + board[right + 1:], left - 1)
        return board

    def dfs(self, board: str, hand: str, memo: dict) -> int:
        if not board:
            return 0
        if not hand:
            return -1

        key = board + "#" + hand
        if key in memo:
            return memo[key]

        minSteps = float("inf")
        for i in range(len(board)):
            for j in range(len(hand)):
                if j > 0 and hand[j] == hand[j - 1]:
                    continue
                if hand[j] == board[i] or (i > 0 and board[i] == board[i - 1] and hand[j] != board[i]):
                    newBoard = self.removeBalls(board[:i] + hand[j] + board[i:], i)
                    if not newBoard:
                        memo[key] = 1
                        return 1
                    nextSteps = self.dfs(newBoard, hand[:j] + hand[j + 1:], memo)
                    if nextSteps != -1:
                        minSteps = min(minSteps, 1 + nextSteps)

        memo[key] = minSteps if minSteps != float("inf") else -1
        return memo[key]
