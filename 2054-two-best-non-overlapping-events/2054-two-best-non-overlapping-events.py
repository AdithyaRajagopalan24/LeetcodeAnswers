from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0])
        maxVals = [0] * n
        maxSum = 0

        maxVals[n - 1] = events[n - 1][2]
        for i in range(n - 2, -1, -1):
            maxVals[i] = max(events[i][2], maxVals[i + 1])
        for i in range(n):
            left, right = i + 1, n - 1
            nextPos = -1
            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] > events[i][1]:
                    nextPos = mid
                    right = mid - 1
                else:
                    left = mid + 1   
            if nextPos != -1:
                maxSum = max(maxSum, events[i][2] + maxVals[nextPos])     
            maxSum = max(maxSum, events[i][2])  
        return maxSum