class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        self.intervals.append([value, value])

    def getIntervals(self) -> List[List[int]]:
        if len(self.intervals) == 0:
            return []
        self.intervals.sort()
        res = [self.intervals[0]]
        for interval in self.intervals[1:]:
            if res[-1][1] + 1 >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        self.intervals = res
        return self.intervals