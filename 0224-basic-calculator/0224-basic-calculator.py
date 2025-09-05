class Solution:
    def calculate(self, n: int) -> int:
        nextDigit = 10
        currentDigit = 1
        totalOnes = 0

        while (n >= currentDigit):
            div = n // nextDigit
            mod = n % nextDigit
            totalOnes += div * currentDigit
            if mod >= currentDigit:
                totalOnes += min(mod, currentDigit * 2 - 1) - (currentDigit - 1)
            nextDigit *= 10
            currentDigit *= 10

        return totalOnes
