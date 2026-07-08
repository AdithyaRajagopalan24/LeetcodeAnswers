class Solution:
    def hammingWeight(self, n: int) -> int:
        oneCount = 0
        while n > 0:
            oneCount += n & 1
            n = n >> 1
        
        return oneCount