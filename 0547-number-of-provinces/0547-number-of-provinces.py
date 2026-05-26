class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    parent[find(i)] = find(j)

        return sum(find(i) == i for i in range(n))