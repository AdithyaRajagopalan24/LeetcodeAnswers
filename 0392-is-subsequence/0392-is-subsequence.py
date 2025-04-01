class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lastPos = -1
        if len(s) == len(t) and s != t:
            return False
        for i in s:
            if t.find(i, lastPos+1, len(t)) == -1:
                return False
            if t.find(i, lastPos+1, len(t)) < lastPos:
                return False
            lastPos = t.find(i, lastPos + 1, len(t))
        return True