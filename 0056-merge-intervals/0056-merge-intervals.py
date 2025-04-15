class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        finalIntervals = []
        intervals.sort(key=lambda x: x[0])
        latestInterval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= latestInterval[1]:
                latestInterval[1] = max(latestInterval[1], interval[1])
            else:
                finalIntervals.append(latestInterval)
                latestInterval = interval
        finalIntervals.append(latestInterval)
        return finalIntervals