from typing import List, Tuple

class Solution:

    def connectedComponents(self, numNodes: int, graph: List[List[Tuple[int, int]]], timeThreshold: int) -> int:
        visited = [False] * numNodes
        componentCount = 0

        for node in range(numNodes):
            if visited[node]:
                continue

            componentCount, frontierNodes = componentCount + 1, [node]
            while frontierNodes:
                nextFrontier = []
                for curr in frontierNodes:
                    for neighbor, weight in graph[curr]:
                        if visited[neighbor] or weight <= timeThreshold:
                            continue
                        visited[neighbor] = True
                        nextFrontier.append(neighbor)
                frontierNodes = nextFrontier

        return componentCount

    def minTime(self, numNodes: int, edges: List[List[int]], requiredComponents: int) -> int:
        graph = [[] for _ in range(numNodes)]
        maxTime = 0
        for u, v, w in edges:
            maxTime = max(maxTime, w)
            graph[u].append((v, w))
            graph[v].append((u, w))

        low, high = 0, maxTime + 1
        while low < high:
            mid = (low + high) // 2
            componentCount = self.connectedComponents(numNodes, graph, mid)
            if componentCount < requiredComponents:
                low = mid + 1
            else:
                high = mid

        return low
