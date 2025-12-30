class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        charCosts = {}
        totalCost = sum(cost)
        
        for i in range(len(s)):
            charCosts.setdefault(s[i], 0)
            charCosts[s[i]] += cost[i]
        
        minCost = min(totalCost - charCosts.get(char, 0) for char in charCosts)
        return minCost
