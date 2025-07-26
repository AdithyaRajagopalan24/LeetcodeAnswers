from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        conflictEnds = [[] for _ in range(n + 1)]
        for u, v in conflictingPairs:
            conflictEnds[max(u, v)].append(min(u, v))

        totalScore = 0
        forbiddenStarts = [0, 0]
        gainByRemoving = [0] * (n + 1)
        for end in range(1, n + 1):
            for start in conflictEnds[end]:
                if start > forbiddenStarts[0]:
                    forbiddenStarts = [start, forbiddenStarts[0]]
                elif start > forbiddenStarts[1]:
                    forbiddenStarts = [forbiddenStarts[0], start]
            totalScore += end - forbiddenStarts[0]
            if forbiddenStarts[0] > 0:
                gainByRemoving[forbiddenStarts[0]] += forbiddenStarts[0] - forbiddenStarts[1]
        return totalScore + max(gainByRemoving)
