import heapq
from typing import List

class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        graph = [[] for i in range(n)]
        for p, q, r in edges:
            graph[p].append((q, r))

        headerPart = [[] for i in range(n)]
        list1 = [(0, -power, source)]
        bestTime = -1
        bestPower = -1

        while list1:
            passedTime, negativePower, node = heapq.heappop(list1)
            curRemPower = -negativePower

            if bestTime != -1 and passedTime > bestTime:
                break

            isDominated = False
            for newFirst, newSecond in headerPart[node]:
                if newFirst <= passedTime and newSecond >= curRemPower:
                    isDominated = True
                    break
            if isDominated:
                continue

            newHeader = []
            for newFirst, newSecond in headerPart[node]:
                if not (newFirst >= passedTime and newSecond <= curRemPower):
                    newHeader.append((newFirst, newSecond))
            newHeader.append((passedTime, curRemPower))
            headerPart[node] = newHeader

            if node == target:
                if bestTime == -1:
                    bestTime = passedTime
                bestPower = max(bestPower, curRemPower)
                continue
            if curRemPower < cost[node]:
                continue
            newPower = curRemPower - cost[node]
            for nextNode, travelTime in graph[node]:
                finalTime = passedTime + travelTime

                toSkip = False
                for newFirst, newSecond in headerPart[nextNode]:
                    if newFirst <= finalTime and newSecond >= newPower:
                        toSkip = True
                        break
                if not toSkip:
                    heapq.heappush(list1, (finalTime, -newPower, nextNode))
        if bestTime == -1:
            return [-1, -1]
        return [bestTime, bestPower]

        
        # graph = [[] for i in range(n)]
        # maxTotalTime = 0
        # for p, q, r in edges:
        #     graph[p].append((q, r))
        #     maxTotalTime += r

        # def feasibleOrNot(timeLimit: int) -> int:
        #     # leftoverPower = [-1] * n
        #     # leftoverPower[source] = power
        #     headerPart = [[] for i in range(n)]
        #     list1 = [(-power, source, 0)]
        #     optimalPower = -1

        #     foundTime = None

        #     def dominatingPart (firstPart, secondPart, node):
        #         for newFirst, newSecond in headerPart[node]:
        #             if newFirst <= firstPart and newSecond >= secondPart:
        #                 return True
        #         return False

        #     def createNewState (firstPart, secondPart, node):
        #         headerPart[node] = [(newFirst, newSecond) for newFirst, newSecond in headerPart[node] if not (newFirst >= firstPart and newSecond <= secondPart)]
        #         headerPart[node].append((firstPart, secondPart))
                

        #     while list1:
        #         negativePower, node, passedTime = heapq.heappop(list1)
        #         curRemPower = -negativePower

        #         if foundTime is not None and passedTime > foundTime:
        #             break
        #         if dominatingPart(passedTime, curRemPower, node):
        #             continue
        #         createNewState (passedTime, curRemPower, node)
        #         if node == target:
        #             optimalPower = max(optimalPower, curRemPower)
        #             if foundTime is None:
        #                 foundTime = passedTime
        #             continue
        #         if curRemPower < cost[node]:
        #             continue

                
        #         newPower = curRemPower - cost[node]
        #         for nextNode, travelTime in graph[node]:
        #             finalTime = passedTime + travelTime
        #             if finalTime > timeLimit:
        #                 continue
        #             if not dominatingPart(finalTime, newPower, nextNode):
        #                 heapq.heappush(list1, (-newPower, nextNode, finalTime))
        #     return optimalPower

        # leftSide = 0
        # # maxTotalTime = 0
        # rightSide = maxTotalTime
        # bestTime = -1
        # bestPower = -1

        # while leftSide <= rightSide:
        #     midTime = (leftSide + rightSide) // 2
        #     curRemPower = feasibleOrNot(midTime)

        #     if curRemPower != -1:
        #         bestTime = midTime
        #         bestPower = curRemPower
        #         rightSide = midTime - 1
        #     else:
        #         leftSide = midTime + 1

        # if bestTime == -1:
        #     return [-1, -1]
        # return [bestTime, bestPower]
            