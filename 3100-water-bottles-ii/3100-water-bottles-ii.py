class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        totalDrunk = numBottles
        exchangedBottles = 0
        
        while numBottles >= numExchange:
            numBottles = numBottles - numExchange + 1
            numExchange += 1
            exchangedBottles += 1
        
        return totalDrunk + exchangedBottles
