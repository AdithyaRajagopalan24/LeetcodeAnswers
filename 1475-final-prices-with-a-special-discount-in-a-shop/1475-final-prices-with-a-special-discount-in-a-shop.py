class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = list(prices)
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    answer[i] = prices[i] - discount
                    break                
        return answer