class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prevTwo = cost[0]
        prevOne = cost[1]

        for i in range(2, len(cost)):
            current = cost[i] + min(prevOne, prevTwo)
            prevTwo = prevOne
            prevOne = current

        return min(prevOne, prevTwo)