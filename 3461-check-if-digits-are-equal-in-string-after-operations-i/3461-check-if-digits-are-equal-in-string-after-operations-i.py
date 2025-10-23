class Solution:
    def hasSameDigits(self, numStr):
        if len(numStr) < 2:
            return False
        
        digits = [int(ch) for ch in numStr]
        
        while len(digits) > 2:
            nextDigits = [(digits[i] + digits[i + 1]) % 10 for i in range(len(digits) - 1)]
            digits = nextDigits
        
        return digits[0] == digits[1]
