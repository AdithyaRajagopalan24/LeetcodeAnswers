class Solution:
    def isRectangleCover(self, rectangles):
        points, totalArea = set(), 0
        for x1, y1, x2, y2 in rectangles:
            totalArea += (x2 - x1) * (y2 - y1)
            for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)
        if len(points) != 4:
            return False
        xCoords = [p[0] for p in points]
        yCoords = [p[1] for p in points]
        return totalArea == (max(xCoords) - min(xCoords)) * (max(yCoords) - min(yCoords))
