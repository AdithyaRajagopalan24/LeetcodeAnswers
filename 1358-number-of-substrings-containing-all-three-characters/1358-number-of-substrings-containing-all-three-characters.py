class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        substrs = 0
        last_pos = [-1] * 3
        for pos in range(len(s)):
            last_pos[ord(s[pos]) - ord("a")] = pos
            substrs += 1 + min(last_pos)
        return substrs
