class Solution:
    def maximumAND(self, numbers: List[int], budget: int, count: int) -> int:
        result = 0

        for bit in range(30, -1, -1):
            candidate = result | (1 << bit)
            upgradeCosts = []

            for value in numbers:
                updatedValue = value
                cost = 0

                for pos in range(30, bit - 1, -1):
                    if (candidate >> pos) & 1 and not ((updatedValue >> pos) & 1):
                        nextValue = ((updatedValue >> pos) | 1) << pos
                        cost += nextValue - updatedValue
                        updatedValue = nextValue

                upgradeCosts.append(cost)

            upgradeCosts.sort()
            if sum(upgradeCosts[:count]) <= budget:
                result = candidate

        return result
