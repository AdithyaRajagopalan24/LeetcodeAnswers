class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 10 not in {1, 3, 7, 9}:
            return -1
        n = 0
        checkedVals = set()
        for length in range(1, k + 1):
            n = (n * 10 + 1) % k
            if n == 0:
                return length
            if n in checkedVals:
                return -1
            checkedVals.add(n)
        return -1