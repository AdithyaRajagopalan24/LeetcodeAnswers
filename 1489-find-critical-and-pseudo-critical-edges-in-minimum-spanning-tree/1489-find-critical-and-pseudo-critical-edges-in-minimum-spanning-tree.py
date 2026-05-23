class Solution:
    def findCriticalAndPseudoCriticalEdges(self, nodeCount: int, edges: List[List[int]]) -> List[List[int]]:

        edgeCount = len(edges)

        parent = list(range(nodeCount))

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodeA, nodeB):
            parent[find(nodeA)] = find(nodeB)

        graph = [[] for _ in range(nodeCount)]

        def findCycleEdges(currentNode, targetNode, targetWeight, previousNode):

            matchingEdges = []

            if currentNode == targetNode:
                return True, matchingEdges

            for nextNode, edgeWeight, edgeIndex in graph[currentNode]:

                if nextNode == previousNode:
                    continue

                foundPath, collectedEdges = findCycleEdges(currentNode=nextNode, targetNode=targetNode, targetWeight=targetWeight, previousNode=currentNode)

                if foundPath:

                    matchingEdges.extend(collectedEdges)

                    if edgeWeight == targetWeight:
                        matchingEdges.append(edgeIndex)

                    return True, matchingEdges

            return False, matchingEdges

        includedInMST = [0] * edgeCount
        isPseudoCritical = [0] * edgeCount

        minHeap = []

        for edgeIndex, (startNode, endNode, weight) in enumerate(edges):
            heappush(minHeap, (weight, startNode, endNode, edgeIndex))

        remainingEdges = nodeCount - 1

        for _ in range(edgeCount):

            weight, startNode, endNode, edgeIndex = heappop(minHeap)

            includedInMST[edgeIndex] = 1

            if find(startNode) == find(endNode):

                _, cycleEdges = findCycleEdges(startNode, endNode, weight, -1)

                if cycleEdges:

                    isPseudoCritical[edgeIndex] = 1

                    for cycleEdgeIndex in cycleEdges:
                        isPseudoCritical[cycleEdgeIndex] = 1

                else:
                    includedInMST[edgeIndex] = 0

            elif remainingEdges:

                union(startNode, endNode)

                graph[startNode].append((endNode, weight, edgeIndex))
                graph[endNode].append((startNode, weight, edgeIndex))

                remainingEdges -= 1

            else:
                includedInMST[edgeIndex] = 0

        result = [[], []]

        for edgeIndex in range(edgeCount):

            if not includedInMST[edgeIndex]:
                continue

            if isPseudoCritical[edgeIndex]:
                result[1].append(edgeIndex)
            else:
                result[0].append(edgeIndex)

        return result