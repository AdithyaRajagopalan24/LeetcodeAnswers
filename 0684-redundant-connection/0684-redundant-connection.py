class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def join(u, v):
            rootU = find(u)
            rootV = find(v)

            if rootU != rootV:
                if rank[rootU] > rank[rootV]:
                    parent[rootV] = rootU
                elif rank[rootU] < rank[rootV]:
                    parent[rootU] = rootV
                else:
                    parent[rootV] = rootU
                    rank[rootU] += 1

        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            join(u, v)

        return []