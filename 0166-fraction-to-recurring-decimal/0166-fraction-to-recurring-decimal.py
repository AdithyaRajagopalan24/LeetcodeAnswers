class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        negSign = "" if ((numerator < 0) == (denominator < 0)) else "-"
        numerator, denominator = abs(numerator), abs(denominator)
        intValue = str(numerator // denominator)
        remainderIndex, startIndex, lastIndex, decimals, repeating = {}, 0, 0, [], False
        if numerator % denominator == 0:
            return negSign + intValue
        while True:
            decimals.append(numerator // denominator)
            remainder = numerator % denominator
            numerator = remainder * 10
            if remainder == 0:
                repeating = False
                break
            if remainder in remainderIndex:
                repeating = True
                startIndex = remainderIndex[remainder]
                break
            remainderIndex[remainder] = lastIndex
            lastIndex += 1
        decimals = ''.join(list(map(str, decimals[1:])))
        if not repeating:    
            return negSign + intValue + "." + decimals
        non_repeating_part = decimals[:startIndex]
        repeating_part = decimals[startIndex:lastIndex]
        return negSign + intValue + "." + non_repeating_part + f"({repeating_part})"