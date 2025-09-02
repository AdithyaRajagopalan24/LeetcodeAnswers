class Solution:
    def canCompleteCircuit(self, gas, cost):
        totalGas = totalCost = 0
        startIndex = tank = 0

        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                startIndex = i + 1
                tank = 0

        return -1 if totalGas < totalCost else startIndex
