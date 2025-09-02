class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        total = 0

        for i in range(n):
            upper = points[i][1]
            lower = float("-inf")
            for j in range(i + 1, n):
                y = points[j][1]
                if lower < y <= upper:
                    total += 1
                    lower = y
                    if y == upper:
                        break
        return total
