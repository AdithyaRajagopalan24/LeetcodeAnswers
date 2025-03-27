class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        need, matchCnt, left, resStart, resLen = Counter(t), 0, 0, 0, len(s) + 1
        
        for right, ch in enumerate(s):
            if ch in need:
                need[ch] -= 1
                matchCnt += need[ch] == 0

            while matchCnt == len(need):
                curWindowLen = right - left + 1
                if curWindowLen < resLen:
                    resStart, resLen = left, curWindowLen
                removeCh = s[left]
                left += 1 
                if removeCh in need:
                    matchCnt -= need[removeCh] == 0
                    need[removeCh] += 1
        return s[resStart:resStart + resLen] if resLen <= len(s) else ''