from collections import defaultdict, deque

class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        totalCount = 0
        
        nodeValues = defaultdict(int)
        n = len(nums)

        for i in range(n):
            nodeValues[i] = nums[i]

        adjacencyList = defaultdict(list)
        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        allSubsets = []

        def generateSubsets(index, currentSubset):
            if index == n - 1:
                allSubsets.append(currentSubset[:])
                return
            generateSubsets(index + 1, currentSubset + [index + 1])
            generateSubsets(index + 1, currentSubset)

        for i in range(n):
            generateSubsets(i, [i])

        for subset in allSubsets:
            if len(subset) == 1:
                if nodeValues[subset[0]] % 2 == 0:
                    totalCount += 1
                continue

            subsetSum = 0
            for node in subset:
                subsetSum += nodeValues[node]

            subsetSet = set(subset)
            queue = deque([subset[0]])
            visited = set([subset[0]])

            while queue:
                currentNode = queue.popleft()
                for neighbor in adjacencyList[currentNode]:
                    if neighbor in subsetSet and neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

            if subsetSum % 2 == 0 and visited == subsetSet:
                totalCount += 1

        return totalCount