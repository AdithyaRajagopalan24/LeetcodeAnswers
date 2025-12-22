class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strLen = len(strs[0])
        dp = [1] * strLen
        for i in range(1, strLen):
            for j in range(i):
                valid = True
                for row in strs:
                    if row[j] > row[i]:
                        valid = False
                        break
                if valid:
                    dp[i] = max(dp[i], dp[j] + 1)
        return strLen - max(dp)