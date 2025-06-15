class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xorVal = x ^ y
        return bin(xorVal).count('1')