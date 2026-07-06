from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)

            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []