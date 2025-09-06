from functools import lru_cache
from itertools import groupby

class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        groups = tuple((color, len(list(group))) for color, group in groupby(boxes))

        @lru_cache(None)
        def dfs(state: tuple) -> int:
            if not state:
                return 0
            (leftColor, leftLen), rest = state[0], state[1:]
            best = leftLen * leftLen + dfs(rest)
            for idx, (rightColor, rightLen) in enumerate(rest):
                if leftColor == rightColor:
                    best = max(best, dfs(rest[:idx]) + dfs(((leftColor, leftLen + rightLen),) + rest[idx + 1:]))
            return best

        return dfs(groups)
