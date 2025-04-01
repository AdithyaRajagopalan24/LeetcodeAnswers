class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictCounts = {}
        for a in s:
            dictCounts[a] = dictCounts.get(a, 0) + 1
        for i in range(len(s)):
            if dictCounts[s[i]] == 1:
                return i
        return -1