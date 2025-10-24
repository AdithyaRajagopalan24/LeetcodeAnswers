class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA == rootB:
            return
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1


class Solution:
    def maxAlternatingSum(self, nums: list[int], pairs: list[list[int]]) -> int:
        n = len(nums)
        dsu = DSU(n)

        for u, v in pairs:
            dsu.union(u, v)

        groups = {}
        for i in range(n):
            root = dsu.find(i)
            if root not in groups:
                groups[root] = ([], [])
            groups[root][0].append(nums[i])
            groups[root][1].append(i % 2)

        totalSum = 0
        for values, parity in groups.values():
            groupSum = sum(values)
            values.sort(reverse=True)
            evenCount = parity.count(0)
            topEvenSum = sum(values[:evenCount])
            totalSum += 2 * topEvenSum - groupSum

        return totalSum
