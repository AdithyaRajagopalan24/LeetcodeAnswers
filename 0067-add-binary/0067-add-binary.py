class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a, 2) + int(b, 2)
        return (bin(c)[2:])