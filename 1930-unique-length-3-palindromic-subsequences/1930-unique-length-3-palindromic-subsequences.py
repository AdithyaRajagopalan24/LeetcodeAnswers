from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        charIndices = defaultdict(list)
        for i, char in enumerate(s):
            charIndices[char].append(i)
        ans = 0
        for indices in charIndices.values():
            start = indices[0]
            end = indices[-1]
            if end - start <= 1:
                continue
            seen = set()
            for i in range(start + 1, end):
                seen.add(s[i])
            ans += len(seen)
        return ans