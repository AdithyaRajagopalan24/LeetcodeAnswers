from collections import defaultdict
from itertools import pairwise
from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        deltaByY = defaultdict(int)
        totalArea = 0

        for _, y, size in squares:
            totalArea += size * size
            deltaByY[y] += size
            deltaByY[y + size] -= size

        remainingArea = totalArea / 2
        activeWidth = 0

        for lastY, y in pairwise(sorted(deltaByY.keys())):
            activeWidth += deltaByY[lastY]
            remainingArea -= activeWidth * (y - lastY)
            if remainingArea <= 0:
                return y + remainingArea / activeWidth
