from collections import defaultdict
from itertools import product
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowedMap = defaultdict(list)
        for rule in allowed:
            allowedMap[rule[:2]].append(rule[2])
        memo = {}

        def canFormPyramid(bottom):
            if len(bottom) == 1:
                return True
            if bottom in memo:
                return memo[bottom]

            possibleTops = []
            for i in range(1, len(bottom)):
                pair = bottom[i-1] + bottom[i]
                if pair in allowedMap:
                    possibleTops.append(allowedMap[pair])
                else:
                    memo[bottom] = False
                    return False

            for nextTopTuple in product(*possibleTops):
                nextTop = "".join(nextTopTuple)
                if canFormPyramid(nextTop):
                    memo[bottom] = True
                    return True

            memo[bottom] = False
            return False

        return canFormPyramid(bottom)
