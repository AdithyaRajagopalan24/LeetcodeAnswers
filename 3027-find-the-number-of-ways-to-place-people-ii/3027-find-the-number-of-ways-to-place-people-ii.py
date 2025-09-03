class Solution:
    def numberOfPairs(points):
        points.sort(key=lambda p: (p[0], -p[1]))
        pairCount = 0
        pointCount = len(points)

        for leftIndex in range(pointCount):
            upperY = points[leftIndex][1]
            lowerYLimit = float("-inf")

            for rightIndex in range(leftIndex + 1, pointCount):
                currentY = points[rightIndex][1]
                if lowerYLimit < currentY <= upperY:
                    pairCount += 1
                    lowerYLimit = currentY
                    if currentY == upperY:
                        break
        return pairCount