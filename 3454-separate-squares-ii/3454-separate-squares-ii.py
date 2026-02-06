from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xCoords = set()

        for x, y, side in squares:
            events.append((y, 1, x, x + side))
            events.append((y + side, -1, x, x + side))
            xCoords.add(x)
            xCoords.add(x + side)

        events.sort()
        xCoords = sorted(xCoords)
        xIndex = {x: i for i, x in enumerate(xCoords)}
        segmentCount = len(xCoords) - 1

        coverCount = [0] * (4 * segmentCount)
        coverLength = [0] * (4 * segmentCount)

        def update(node, left, right, ql, qr, delta):
            if qr <= left or right <= ql:
                return
            if ql <= left and right <= qr:
                coverCount[node] += delta
            else:
                mid = (left + right) // 2
                update(node * 2, left, mid, ql, qr, delta)
                update(node * 2 + 1, mid, right, ql, qr, delta)

            if coverCount[node] > 0:
                coverLength[node] = xCoords[right] - xCoords[left]
            else:
                coverLength[node] = (
                    coverLength[node * 2] + coverLength[node * 2 + 1]
                    if left + 1 < right else 0
                )

        prevY = events[0][0]
        totalArea = 0.0

        for y, delta, x1, x2 in events:
            height = y - prevY
            if height > 0:
                totalArea += height * coverLength[1]
            update(1, 0, segmentCount, xIndex[x1], xIndex[x2], delta)
            prevY = y

        halfArea = totalArea / 2
        accumulated = 0.0
        prevY = events[0][0]
        coverCount = [0] * (4 * segmentCount)
        coverLength = [0] * (4 * segmentCount)

        for y, delta, x1, x2 in events:
            height = y - prevY
            if height > 0:
                slabArea = height * coverLength[1]
                if accumulated + slabArea >= halfArea:
                    return prevY + (halfArea - accumulated) / coverLength[1]
                accumulated += slabArea
            update(1, 0, segmentCount, xIndex[x1], xIndex[x2], delta)
            prevY = y

        return prevY
 