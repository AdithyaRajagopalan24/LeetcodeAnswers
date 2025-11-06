from typing import List

class Solution:
    def processQueries(self, numCities: int, roads: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(numCities + 1))

        def findRoot(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for cityA, cityB in roads:
            rootA, rootB = findRoot(cityA), findRoot(cityB)
            if rootA != rootB:
                parent[rootB] = rootA

        nextCity = [0] * (numCities + 1)
        compMin = [0] * (numCities + 1)
        lastCity = {}

        for city in range(1, numCities + 1):
            root = findRoot(city)
            if compMin[root] == 0:
                compMin[root] = city
            else:
                nextCity[lastCity[root]] = city
            lastCity[root] = city

        isOffline = [False] * (numCities + 1)
        result = []

        for queryType, city in queries:
            if queryType == 1:
                if not isOffline[city]:
                    result.append(city)
                else:
                    root = findRoot(city)
                    minCity = compMin[root]
                    result.append(minCity if minCity else -1)
            else:
                if isOffline[city]:
                    continue
                isOffline[city] = True
                root = findRoot(city)
                if compMin[root] == city:
                    nextAvailable = nextCity[city]
                    while nextAvailable and isOffline[nextAvailable]:
                        nextAvailable = nextCity[nextAvailable]
                    compMin[root] = nextAvailable

        return result
