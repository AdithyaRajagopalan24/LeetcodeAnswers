class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        charCount = Counter(s)
        finalAns = []
        for curChar in s:
            while finalAns and finalAns[-1] > curChar and charCount[finalAns[-1]] >= 2:
                charCount[finalAns[-1]] -= 1
                finalAns.pop()
            finalAns.append(curChar)
        while charCount[finalAns[-1]] >= 2:
            charCount[finalAns[-1]] -= 1
            finalAns.pop()
        return "".join(finalAns)