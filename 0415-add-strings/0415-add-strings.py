import sys
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(0)
        finalVal = 0
        minLength = min(len(num1), len(num2))     
        for i in range(-1, -1*(minLength+1), -1):
            digSum = int(num1[i]) + int(num2[i])
            if (int(num1[i]) + int(num2[i])) >= 10:
                finalVal += ((10**((i)*-1)) + ((10**((i+1)*-1))*(digSum-10)))
            else:
                finalVal += ((10**((i+1)*-1))*digSum)
        if (minLength == len(num1)):
            for i in range(minLength, len(num2)):
                finalVal += ((10**(i))*int(num2[(len(num2) - i - 1)]))
        else:
            for i in range(minLength, len(num1)):
                finalVal += (10**(i)*int(num1[(len(num1) - i - 1)]))
        return(str(finalVal))