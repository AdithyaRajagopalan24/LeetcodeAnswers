class Solution:
    def combine(self, n: int, k: int):
        result = []
        curr = [0] * k 
        self.dfs(1, 0, n, k, curr, result)
        return result

    def dfs(self, start, depth, n, k, curr, result):
        if depth == k:
            result.append(curr[:])
            return
        for i in range(start, n - (k - depth) + 2):
            curr[depth] = i
            self.dfs(i + 1, depth + 1, n, k, curr, result)