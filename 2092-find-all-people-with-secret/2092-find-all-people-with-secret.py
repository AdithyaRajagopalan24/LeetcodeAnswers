from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        peopleWithSecret = set([0, firstPerson])
        meetingsByTime = defaultdict(list)

        for x, y, t in meetings:
            meetingsByTime[t].append((x, y))

        for time in sorted(meetingsByTime):
            graph = defaultdict(list)
            for x, y in meetingsByTime[time]:
                graph[x].append(y)
                graph[y].append(x)

            visited = set()
            for person in graph:
                if person in visited:
                    continue
                queue = deque([person])
                component = set([person])
                visited.add(person)

                while queue:
                    curr = queue.popleft()
                    for nei in graph[curr]:
                        if nei not in visited:
                            visited.add(nei)
                            component.add(nei)
                            queue.append(nei)

                if component & peopleWithSecret:
                    peopleWithSecret |= component

        return list(peopleWithSecret)
