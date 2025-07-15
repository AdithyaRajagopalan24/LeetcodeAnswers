class Solution:
    def minCost(self, N: int, edges: List[List[int]], k: int) -> int:
        def find(a):
            if parents[a] != a:
                parents[a] = find(parents[a])
            return parents[a]
        def union(a, b):
            if (ra := find(a)) == (rb := find(b)):
                return False
            parents[ra] = rb
            return True

        parents = list(range(N))
        count = N
        edges.sort(key=lambda x: x[-1]) 
        last_t = 0
        for a,b,t in edges:
            if count > k: 
                if union(a,b):
                    count -= 1
            else:
                break
            last_t = t
        return last_t