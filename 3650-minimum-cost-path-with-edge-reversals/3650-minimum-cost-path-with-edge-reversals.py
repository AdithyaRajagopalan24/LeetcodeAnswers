class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for fromNode, toNode, weight in edges:
            adjList[fromNode].append((toNode, weight))
            adjList[toNode].append((fromNode, 2 * weight))

        minDist = [math.inf] * n
        minDist[0] = 0

        minHeap = [(0, 0)]
        while minHeap:
            currentDist, currentNode = heapq.heappop(minHeap)
            if currentNode == n - 1:
                return currentDist
            if currentDist != minDist[currentNode]:
                continue
            for nextNode, edgeWeight in adjList[currentNode]:
                newDist = currentDist + edgeWeight
                if newDist < minDist[nextNode]:
                    minDist[nextNode] = newDist
                    heapq.heappush(minHeap, (newDist, nextNode))

        return -1
