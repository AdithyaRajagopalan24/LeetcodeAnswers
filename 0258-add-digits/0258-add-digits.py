class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        curNum = (num)
        tempNum = 0
        while((curNum)//10 >= 1):
            curNum = (curNum)%9 + 9
            if (curNum == tempNum):
                return curNum-9
            tempNum = curNum
        return curNum