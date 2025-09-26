from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        seenPoints = []
        slopeCounts = defaultdict(int)
        lineCounts = defaultdict(int)
        slopeSideCounts = defaultdict(int)
        lineSideCounts = defaultdict(int)
        
        trapezoidCount = 0
        rhombusCount = 0
        
        for x1, y1 in points:
            for x2, y2 in seenPoints:
                slope = ((y1 - y2) / (x1 - x2)) if x1 != x2 else "inf"
                intercept = (y1 - slope * x1) if slope != "inf" else x1
                slope = round(slope, 8) if slope != "inf" else slope
                intercept = round(intercept, 8)

                otherSideCount = slopeCounts[slope] - lineCounts[(slope, intercept)]
                trapezoidCount += otherSideCount

                slopeCounts[slope] += 1
                lineCounts[(slope, intercept)] += 1

                dx, dy = abs(x1 - x2), abs(y1 - y2)
                sideLengthSq = dx * dx + dy * dy
                rhombusCount += slopeSideCounts[(slope, sideLengthSq)] - lineSideCounts[(slope, intercept, sideLengthSq)]

                slopeSideCounts[(slope, sideLengthSq)] += 1
                lineSideCounts[(slope, intercept, sideLengthSq)] += 1
                
            seenPoints.append((x1, y1))

        return trapezoidCount - rhombusCount // 2
