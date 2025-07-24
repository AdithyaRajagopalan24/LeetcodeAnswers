import collections

class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        subtreeXor = [0] * n
        nodeDescendants = [set() for _ in range(n)]

        def dfs(current, parent):
            subtreeXor[current] = nums[current]
            nodeDescendants[current].add(current)

            for neighbor in graph[current]:
                if neighbor != parent:
                    dfs(neighbor, current)
                    subtreeXor[current] ^= subtreeXor[neighbor]
                    nodeDescendants[current].update(nodeDescendants[neighbor])

        dfs(0, -1)

        totalXor = subtreeXor[0]
        minDiff = float('inf')

        for i in range(1, n):
            for j in range(i + 1, n):
                xor1 = subtreeXor[i]
                xor2 = subtreeXor[j]

                if j in nodeDescendants[i]:
                    a, b, c = xor2, xor1 ^ xor2, totalXor ^ xor1
                elif i in nodeDescendants[j]:
                    a, b, c = xor1, xor2 ^ xor1, totalXor ^ xor2
                else:
                    a, b, c = xor1, xor2, totalXor ^ xor1 ^ xor2

                minDiff = min(minDiff, max(a, b, c) - min(a, b, c))

        return minDiff
