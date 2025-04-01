class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factorVal in [2, 3, 5]:
            while n % factorVal == 0:
                n //= factorVal
        return n == 1