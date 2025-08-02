class Solution:
    def minCost(self, source: List[int], target: List[int]) -> int:
        from collections import Counter
        diff = Counter(source) - Counter(target)
        diff += Counter(target) - Counter(source)
        if any(count % 2 for count in diff.values()):
            return -1

        excess = []
        minElem = min(source + target)
        for num, count in diff.items():
            excess += [num] * (count // 2)
        excess.sort()
        return sum(min(x, 2 * minElem) for x in excess[:len(excess) // 2])
