import math
from itertools import combinations

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        triplets = list(combinations(arr, 3))
        goodTriplets = 0
        for triplets1 in triplets:
            differences = [abs(triplets1[0] - triplets1[1]), abs(triplets1[1] - triplets1[2]), abs(triplets1[2] - triplets1[0])]
        # differences = [abs(triplets - triplets.next()), abs(triplets.next() - triplets.next().next()), abs(triplets.next().next() - triplets)]
            differencesCombi = list(combinations(differences, 3))
            for i in differencesCombi:
                if i[0] <= a and i[1] <= b and i[2] <= c:
                    goodTriplets += 1
                    continue
        return goodTriplets