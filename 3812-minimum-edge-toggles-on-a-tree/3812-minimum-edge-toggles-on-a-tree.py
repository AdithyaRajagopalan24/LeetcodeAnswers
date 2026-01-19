class Solution:
    def depthFirstSearch(self, flipEdges, diff, adjList, currentNode, parentNode):
        flipParity = diff[currentNode]
        for nextNode, edgeIndex in adjList[currentNode]:
            if nextNode == parentNode:
                continue
            if self.depthFirstSearch(flipEdges, diff, adjList, nextNode, currentNode):
                flipParity ^= 1
                flipEdges.append(edgeIndex)
        return flipParity

    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        diff = [start[i] != target[i] for i in range(len(start))]
        adjList = [[] for _ in range(n)]
        for edgeIndex, (u, v) in enumerate(edges):
            adjList[u].append((v, edgeIndex))
            adjList[v].append((u, edgeIndex))
        flipEdges = []
        if self.depthFirstSearch(flipEdges, diff, adjList, 0, -1):
            return [-1]
        return sorted(flipEdges)
