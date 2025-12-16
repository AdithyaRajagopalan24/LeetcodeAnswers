from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        employeeTree = [[] for i in range(n)]
        for u, v in hierarchy:
            employeeTree[u - 1].append(v - 1)
        dp = [[[0] * (budget + 1) for i in range(2)] for j in range(n)]
        self.dfs(0, present, future, employeeTree, dp, budget)
        return max(dp[0][0])

    def dfs(self, u, present, future, employeeTree, dp, budget):
        children = employeeTree[u]
        childDPS = []
        for i in children:
            self.dfs(i, present, future, employeeTree, dp, budget)
            childDPS.append((dp[i][0], dp[i][1]))

        for parentBought in range(2):
            price = present[u] // 2 if parentBought else present[u]
            profit = future[u] - price
            base = [0] * (budget + 1)
            for i, j in childDPS:
                minNextTreePart = [0] * (budget + 1)
                for b in range(budget + 1):
                    if base[b] == 0 and b != 0:
                        continue
                    for k in range(budget - b + 1):
                        minNextTreePart[b + k] = max(minNextTreePart[b + k], base[b] + i[k])
                base = minNextTreePart

            curr = base[:]

            if price <= budget:
                base = [0] * (budget + 1)
                for i, j in childDPS:
                    minNextTreePart = [0] * (budget + 1)
                    for b in range(budget + 1):
                        if base[b] == 0 and b != 0:
                            continue
                        for k in range(budget - b + 1):
                            minNextTreePart[b + k] = max(minNextTreePart[b + k], base[b] + j[k])
                    base = minNextTreePart

                for b in range(price, budget + 1):
                    curr[b] = max(curr[b], base[b - price] + profit)
            dp[u][parentBought] = curr