class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numExchange <= 1:
            return float('inf')
        return numBottles + (numBottles - 1) // (numExchange - 1)