class Solution:
    def numOfSubsequences(self, s: str) -> int:
        if len(s) < 2:
            return 0

        n = len(s)

        lCount, lcCount, lctCount = 0, 0, 0

        for ch in s:
            if ch == "L":
                lCount += 1
            elif ch == "C":
                lcCount += lCount
            elif ch == "T":
                lctCount += lcCount

        ctCount = 0
        cCount = 0
        for ch in s:
            if ch == "C":
                cCount += 1
            if ch == "T":
                ctCount += cCount

        caseOne = lctCount + ctCount
        caseThree = lctCount + lcCount

        prefixL = 0
        suffixT = s.count("T")
        maxExtra = 0
        for i in range(len(s) + 1):
            if i < len(s):
                if s[i] == "L":
                    prefixL += 1
                elif s[i] == "T":
                    suffixT -= 1

            maxExtra = max(maxExtra, prefixL * suffixT)

        caseTwo = lctCount + maxExtra

        return max(lctCount, caseOne, caseTwo, caseThree)
