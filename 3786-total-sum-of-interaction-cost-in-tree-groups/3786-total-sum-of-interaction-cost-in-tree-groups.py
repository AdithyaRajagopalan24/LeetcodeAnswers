from math import isqrt
from typing import List

class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        groupCount = [0] * 21
        for g in group:
            groupCount[g] += 1
        
        inTime = [0] * n
        outTime = [0] * n
        dfsOrder = [0] * n
        self.time = 0
        
        def dfs(node, parent):
            inTime[node] = self.time
            dfsOrder[self.time] = node
            self.time += 1
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
            outTime[node] = self.time - 1
        
        dfs(0, -1)
        
        groupInOrder = [0] * n
        for i, node in enumerate(dfsOrder):
            groupInOrder[i] = group[node]
        
        queries = []
        for u, v in edges:
            if inTime[u] > inTime[v]:
                u, v = v, u
            queries.append([inTime[v], outTime[v] + 1])
        
        numQueries = len(queries)
        blockSize = n // isqrt(numQueries + 1) + 1
        
        queries.sort(key=lambda x: (x[0] // blockSize, x[1] if (x[0] // blockSize) % 2 == 0 else -x[1]))
        
        left, right = 0, 0
        self.pairSum = 0
        groupCountInRange = [0] * 21
        
        def add(node):
            groupValue = groupInOrder[node]
            self.pairSum -= groupCount[groupValue] * groupCountInRange[groupValue]
            groupCount[groupValue] -= 1
            groupCountInRange[groupValue] += 1
            self.pairSum += groupCount[groupValue] * groupCountInRange[groupValue]
        
        def remove(node):
            groupValue = groupInOrder[node]
            self.pairSum -= groupCount[groupValue] * groupCountInRange[groupValue]
            groupCount[groupValue] += 1
            groupCountInRange[groupValue] -= 1
            self.pairSum += groupCount[groupValue] * groupCountInRange[groupValue]
        
        result = 0
        for queryLeft, queryRight in queries:
            while right < queryRight:
                add(right)
                right += 1
            while left > queryLeft:
                left -= 1
                add(left)
            while right > queryRight:
                right -= 1
                remove(right)
            while left < queryLeft:
                remove(left)
                left += 1
            result += self.pairSum
        
        return result
