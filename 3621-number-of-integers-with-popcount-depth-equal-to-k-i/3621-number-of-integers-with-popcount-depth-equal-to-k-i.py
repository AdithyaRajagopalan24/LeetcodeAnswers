class Solution:
    def popcountDepth(self, num: int, depth: int) -> int:
        if depth == 0:
            return 1

        def getDepth(val: int) -> int:
            steps = 0
            while val > 1:
                val = bin(val).count('1')
                steps += 1
            return steps

        targetCounts = {c for c in range(1, 65) if getDepth(c) == depth - 1}
        if not targetCounts:
            return 0

        bits = bin(num)[2:]

        @cache
        def dfs(index: int, isTight: bool, ones: int) -> int:
            if index == len(bits):
                return 1 if ones in targetCounts else 0
            limit = int(bits[index]) if isTight else 1
            total = 0
            for bit in range(limit + 1):
                total += dfs(index + 1, isTight and bit == limit, ones + bit)
            return total

        result = dfs(0, True, 0)
        return result - 1 if depth == 1 and 1 in targetCounts else result
