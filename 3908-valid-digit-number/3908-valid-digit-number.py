class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        nStr, xStr = str(n), str(x)
        if nStr[0] == xStr: return False
        for char in nStr:
            if char == xStr: return True
        return False