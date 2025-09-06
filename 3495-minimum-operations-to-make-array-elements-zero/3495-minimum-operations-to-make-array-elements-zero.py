from math import log
from typing import List

pow4 = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576,
        4194304, 16777216, 67108864, 268435456, 1073741824, 4294967296]

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def calcRange(left, right):
            l, r = int(log(left, 4)) + 1, int(log(right, 4))
            if l - 1 == r:
                total = (right + 1 - left) * l
            else:
                total = l * (pow4[l] - left) + (r + 1) * (right + 1 - pow4[r])
                for k in range(l + 1, r + 1):
                    total += 3 * k * pow4[k - 1]
            return (total + 1) // 2

        return sum(calcRange(l, r) for l, r in queries)
