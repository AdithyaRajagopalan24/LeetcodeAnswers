class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dfs(idx, mask, remaining):
            if idx >= n:
                return 0
            if (idx, mask, remaining) in memo:
                return memo[(idx, mask, remaining)]

            charIdx = ord(s[idx]) - ord('a')
            charBit = 1 << charIdx
            newMask = mask | charBit
            distinctCount = newMask.bit_count()

            if distinctCount > k:
                skip = 1 + dfs(idx + 1, charBit, remaining)
            else:
                skip = dfs(idx + 1, newMask, remaining)

            pick = 0
            if remaining > 0:
                for c in range(26):
                    bit = 1 << c
                    newMask = mask | bit
                    distinctCount = newMask.bit_count()
                    if distinctCount > k:
                        pick = max(pick, 1 + dfs(idx + 1, bit, remaining - 1))
                    else:
                        pick = max(pick, dfs(idx + 1, newMask, remaining - 1))

            memo[(idx, mask, remaining)] = max(skip, pick)
            return memo[(idx, mask, remaining)]

        n = len(s)
        memo = {}
        return 1 + dfs(0, 0, 1)
    