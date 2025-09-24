class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        num = abs(numerator)
        den = abs(denominator)
        quotient, remainder = divmod(num, den)
        result.append(str(quotient))
        if remainder == 0:
            return "".join(result)
        result.append(".")
        seen = {}
        fraction = []
        while remainder != 0:
            if remainder in seen:
                fraction.insert(seen[remainder], "(")
                fraction.append(")")
                break
            seen[remainder] = len(fraction)
            remainder *= 10
            fraction.append(str(remainder // den))
            remainder %= den
        return "".join(result + fraction)
