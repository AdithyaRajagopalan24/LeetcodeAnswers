class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        halfVal = k // 2
        prefixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + strategy[i] * prices[i]
        windowSum = sum(prices[halfVal:k])
        maxProfit = max(prefixSum[n], windowSum + prefixSum[n] - prefixSum[k])
        
        for start in range(1, n - k + 1):
            windowSum += prices[start + k - 1] - prices[start + halfVal - 1]
            maxProfit = max(maxProfit, windowSum + prefixSum[n] - prefixSum[start + k] + prefixSum[start])
            
        return maxProfit