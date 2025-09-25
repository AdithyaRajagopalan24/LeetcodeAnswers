class Solution:
    def minimumTotal(self, mat: List[List[int]]) -> int:
        dp = mat[-1][:]  
        for i in range(len(mat) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = mat[i][j] + min(dp[j], dp[j + 1])
        return dp[0]
