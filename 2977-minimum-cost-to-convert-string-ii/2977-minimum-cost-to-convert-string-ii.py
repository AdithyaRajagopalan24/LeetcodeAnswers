class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        base = 27
        mask = (1 << 32) - 1
        inf = 10**10

        def getHash(s):
            h = 0
            for c in s:
                h = (h * base + (ord(c) - 96)) & mask
            return h

        graph = {getHash(chr(i + 97)): {getHash(chr(i + 97)): 0} for i in range(26)}
        allItems = set()

        for i in range(len(cost)):
            u = getHash(original[i])
            v = getHash(changed[i])
            allItems.add(u)
            allItems.add(v)
            graph.setdefault(u, {})
            graph[u][v] = min(graph[u].get(v, inf), cost[i])

        graphKeys = list(graph.keys())
        allItems = list(allItems)

        for k in allItems:
            if k not in graph:
                continue
            for i in graphKeys:
                if k not in graph[i]:
                    continue
                ik = graph[i][k]
                for j, kj in graph[k].items():
                    val = ik + kj
                    if j in graph[i]:
                        graph[i][j] = min(graph[i][j], val)
                    else:
                        graph[i][j] = val

        n = len(source)
        powBase = [1] * (n + 1)
        for i in range(1, n + 1):
            powBase[i] = (powBase[i - 1] * base) & mask

        prefixSource = [0] * (n + 1)
        prefixTarget = [0] * (n + 1)

        for i in range(1, n + 1):
            prefixSource[i] = (prefixSource[i - 1] * base + (ord(source[i - 1]) - 96)) & mask
            prefixTarget[i] = (prefixTarget[i - 1] * base + (ord(target[i - 1]) - 96)) & mask

        def subHash(p, l, r):
            return (p[r] - p[l] * powBase[r - l]) & mask

        dp = [inf] * (n + 1)
        dp[0] = 0

        lengths = sorted({len(s) for s in original} | {1})

        for j in range(1, n + 1):
            for L in lengths:
                i = j - L
                if i < 0:
                    break
                u = subHash(prefixSource, i, j)
                v = subHash(prefixTarget, i, j)
                if u == v:
                    dp[j] = min(dp[j], dp[i])
                elif u in graph and v in graph[u]:
                    dp[j] = min(dp[j], dp[i] + graph[u][v])

        return dp[n] if dp[n] != inf else -1
