from collections import deque, defaultdict

class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k):
        if n < 2:
            return 1    
        graph = defaultdict(list)
        degrees = [0] * n     
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1 
        nodeValues = values[:]
        leafQueue = deque([i for i in range(n) if degrees[i] == 1])
        componentCount = 0
   
        while leafQueue:
            node = leafQueue.popleft()
            degrees[node] -= 1
            carryValue = 0
            if nodeValues[node] % k == 0:
                componentCount += 1
            else:
                carryValue = nodeValues[node]
            for neighbor in graph[node]:
                if degrees[neighbor] == 0:
                    continue
                degrees[neighbor] -= 1
                nodeValues[neighbor] += carryValue
                if degrees[neighbor] == 1:
                    leafQueue.append(neighbor)
        return componentCount