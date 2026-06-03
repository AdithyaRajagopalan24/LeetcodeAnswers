class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removedCount = 0

        intervals.sort(key=lambda interval: interval[1])
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                removedCount += 1
            else:
                prevEnd = intervals[i][1]

        return removedCount