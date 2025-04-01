class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        areaFirst = abs(ax1 - ax2) * abs(ay1 - ay2)
        areaSecond = abs(bx1 - bx2) * abs(by1 - by2)
        xDistance = (min(ax2, bx2) -max(ax1, bx1))
        yDistance = (min(ay2, by2) -max(ay1, by1))
        area = 0
        if xDistance > 0 and yDistance > 0:
            area = xDistance * yDistance
        return (areaFirst + areaSecond - area)