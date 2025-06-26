class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = cur = 0
        for c in reversed(s):
            if c == '0': 
                res += 1
            else:
                if cur + (1 << res) <= k:
                    cur += 1 << res
                    res += 1
        return res