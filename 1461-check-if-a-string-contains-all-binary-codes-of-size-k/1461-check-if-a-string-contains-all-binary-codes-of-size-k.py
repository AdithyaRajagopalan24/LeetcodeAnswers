class Solution:
    def hasAllCodes(self, binaryString: str, codeLength: int) -> bool:
        stringLength = len(binaryString)
        uniqueCodes = set()

        for index in range(stringLength - codeLength + 1):
            substring = binaryString[index:index + codeLength]
            uniqueCodes.add(substring)

        return len(uniqueCodes) == 2 ** codeLength