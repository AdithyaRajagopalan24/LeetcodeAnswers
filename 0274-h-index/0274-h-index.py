class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        total = 0
        storer = [0 for _ in range(n + 1)]

        for i,v in enumerate(citations):
            if v > n :
                storer[n] += 1
            else:
                storer[v] += 1
        for i in range(n, -1, -1):
            total += storer[i]
            if total >= i:
                return i