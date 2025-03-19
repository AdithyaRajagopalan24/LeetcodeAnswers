class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x in range(1, 4):
            return 1
        elif x == 4 or x == 5:
            return 2
        else:
            for i in range(2, x):
                if (i*i)==x:
                    return i
                elif (i*i)>x:
                    return (i-1)
        