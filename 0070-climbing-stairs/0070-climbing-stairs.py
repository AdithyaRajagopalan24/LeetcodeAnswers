class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 :
            return 1
        if n==2 :
            return 2
        num1 = 1
        num2 = 2
        numOfWays = 0
        for i in range(3 ,n+1):
            numOfWays=num1 + num2
            num1 = num2
            num2 = numOfWays
        return numOfWays
