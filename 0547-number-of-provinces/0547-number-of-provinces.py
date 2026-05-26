class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pb] = pa

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i, j)

        provinces = 0
        for i in range(n):
            if find(i) == i:
                provinces += 1

        return provinces