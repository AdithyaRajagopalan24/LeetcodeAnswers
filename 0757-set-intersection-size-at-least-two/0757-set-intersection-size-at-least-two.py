class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: (x[1], x[0]))
        firstPoint, secondPoint = -math.inf, -math.inf
        count = 0

        for start, end in intervals:
            if not (start <= secondPoint <= end):
                count += 2
                firstPoint = end - 1
                secondPoint = end
            elif not (start <= firstPoint <= end):
                count += 1
                firstPoint = min(secondPoint, end - 1)
                secondPoint = end

        return count
