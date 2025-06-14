class Solution:
    def minMaxDifference(self, num: int) -> int:
        numStr = str(num)
        digitToReplaceForMax = ''
        for digit in numStr:
            if digit != '9':
                digitToReplaceForMax = digit
                break
        maxTransformedStr = ''.join(['9' if digit == digitToReplaceForMax else digit for digit in numStr])
        digitToReplaceForMin = numStr[0]
        minTransformedStr = ''.join(['0' if digit == digitToReplaceForMin else digit for digit in numStr])

        return int(maxTransformedStr) - int(minTransformedStr)
