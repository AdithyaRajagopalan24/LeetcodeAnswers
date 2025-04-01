class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n-1
        multiplesOf3 = n//3
        if n%3 == 0:
            return 3**multiplesOf3
        if n%3 == 1:
            return (3**(multiplesOf3-1))*4
        else:
            return (3**multiplesOf3)*2