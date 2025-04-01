class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        storeCount = 0
        for byte in data:
            temp = 128  # 0b10000000
            oneCount = 0
            while byte & temp != 0:
                oneCount += 1
                temp >>= 1
            if oneCount > 4:
                return False
            elif oneCount > 1:
                if storeCount != 0:
                    return False
                storeCount = oneCount - 1
            elif oneCount == 0:
                if storeCount != 0:
                    return False
            else:
                if storeCount >= 1:
                    storeCount -= 1
                else:
                    return False
        return storeCount == 0
