import heapq
from collections import defaultdict

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], maxTotalCost: int) -> int:
        graph = defaultdict(list)
        maxEdgeCost = float('-inf')
        
        for start, end, cost in edges:
            if online[start] and online[end]:
                graph[start].append([end, cost])
                maxEdgeCost = max(maxEdgeCost, cost)
        
        targetNode = len(online) - 1

        def isValid(minScore: int) -> bool:
            heap = [[0, 0]]
            minCost = {0: 0}
            
            while heap:
                totalCost, node = heapq.heappop(heap)
                if node == targetNode:
                    return True
                if totalCost > minCost.get(node, float('inf')):
                    continue
                for neighbor, edgeCost in graph[node]:
                    if edgeCost >= minScore:
                        newCost = totalCost + edgeCost
                        if newCost <= maxTotalCost and newCost < minCost.get(neighbor, float('inf')):
                            minCost[neighbor] = newCost
                            heapq.heappush(heap, [newCost, neighbor])
            return False

        lowerBound = float('-inf')
        result = -1
        costMap = defaultdict(lambda: float('inf'))
        scoreMap = defaultdict(lambda: float('-inf'))
        costMap[0] = 0
        scoreMap[0] = float('inf')
        heap = [[0, 0]]
        
        while heap:
            totalCost, node = heapq.heappop(heap)
            if totalCost > costMap[node]:
                continue
            for neighbor, edgeCost in graph[node]:
                newCost = totalCost + edgeCost
                if newCost <= maxTotalCost and newCost < costMap[neighbor]:
                    costMap[neighbor] = newCost
                    scoreMap[neighbor] = min(scoreMap[node], edgeCost)
                    heapq.heappush(heap, [newCost, neighbor])
        
        if targetNode in scoreMap:
            lowerBound = scoreMap[targetNode]
            result = lowerBound

        while lowerBound <= maxEdgeCost:
            midScore = (lowerBound + maxEdgeCost) // 2
            if isValid(midScore):
                result = midScore
                lowerBound = midScore + 1
            else:
                maxEdgeCost = midScore - 1

        return result
