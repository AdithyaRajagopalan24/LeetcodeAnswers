import re
from math import gcd

class Solution:
    _fractionPattern = re.compile(r'[+-]?\d+/\d+')

    def fractionAddition(self, expression: str) -> str:
        sumNum, sumDen = 0, 1
        for token in self._fractionPattern.findall(expression):
            termNum, termDen = map(int, token.split('/'))
            g = gcd(sumDen, termDen)
            lcmDen = (sumDen // g) * termDen
            sumNum = sumNum * (lcmDen // sumDen) + termNum * (lcmDen // termDen)
            sumDen = lcmDen
            g2 = gcd(abs(sumNum), sumDen)
            sumNum //= g2
            sumDen //= g2
        return f"{sumNum}/{sumDen}"
