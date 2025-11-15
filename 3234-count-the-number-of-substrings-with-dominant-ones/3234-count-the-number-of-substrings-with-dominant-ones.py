class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        stringLength = len(s)
        prefixZeroBoundary = [-1] * (stringLength + 1)

        for i in range(stringLength):
            if i == 0 or s[i - 1] == "0":
                prefixZeroBoundary[i + 1] = i
            else:
                prefixZeroBoundary[i + 1] = prefixZeroBoundary[i]

        resultCount = 0
        
        for i in range(1, stringLength + 1):
            countZeros = 1 if s[i - 1] == "0" else 0
            leftBoundary = i
            
            while leftBoundary > 0 and countZeros * countZeros <= stringLength:
                segmentStartIndex = prefixZeroBoundary[leftBoundary]
                
                countOnes = (i - segmentStartIndex) - countZeros
                
                if countZeros * countZeros <= countOnes:
                    maxValidSegments = countOnes - countZeros * countZeros + 1
                    resultCount += min(leftBoundary - segmentStartIndex, maxValidSegments)
                
                leftBoundary = segmentStartIndex
                countZeros += 1
                
        return resultCount