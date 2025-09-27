import math
from typing import List

class Solution:
    def getLength(self, pointA, pointB):
        x1, y1 = pointA
        x2, y2 = pointB
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def getSlope(self, pointA, pointB):
        x1, y1 = pointA
        x2, y2 = pointB
        return (y1 - y2) / (x1 - x2) if x1 != x2 else float("inf")

    def isValidTriangle(self, pointA, pointB, pointC):
        return self.getSlope(pointA, pointB) != self.getSlope(pointA, pointC)

    def getArea(self, sideA, sideB, sideC):
        semiPerimeter = (sideA + sideB + sideC) / 2
        return math.sqrt(
            semiPerimeter
            * (semiPerimeter - sideA)
            * (semiPerimeter - sideB)
            * (semiPerimeter - sideC)
        )

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = 0
        n = len(points)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    p1, p2, p3 = points[i], points[j], points[k]
                    if self.isValidTriangle(p1, p2, p3):
                        sideA = self.getLength(p1, p2)
                        sideB = self.getLength(p2, p3)
                        sideC = self.getLength(p1, p3)
                        area = self.getArea(sideA, sideB, sideC)
                        maxArea = max(maxArea, area)
        return maxArea
