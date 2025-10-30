class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = previousVal = 0
        for i in target:
            if i > previousVal:
                ans += i - previousVal
            previousVal = i
        return ans