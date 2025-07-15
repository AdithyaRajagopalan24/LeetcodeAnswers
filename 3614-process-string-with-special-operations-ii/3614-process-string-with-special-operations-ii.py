class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        for char in s:
            if char == '*':
                if length:
                    length -= 1
            elif char == '#':
                length *= 2
            elif char == '%':
                pass
            else:
                length += 1
        
        if k >= length:
            return '.'
        
        for char in reversed(s):
            if char == '*':
                length += 1
            elif char == '#':
                half = length // 2
                if k >= half:
                    k -= half
                length = half
            elif char == '%':
                k = length - k - 1
            else:
                if k == length - 1:
                    return char
                length -= 1