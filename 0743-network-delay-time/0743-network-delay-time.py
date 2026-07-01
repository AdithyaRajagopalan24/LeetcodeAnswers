class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}

        for start, end, travel in times:
            graph.setdefault(start, []).append((end, travel))

        shortest = {}
        pq = [(0, k)]
        longest = 0

        while pq:
            currentTime, node = heapq.heappop(pq)

            if node in shortest:
                continue

            shortest[node] = currentTime
            longest = max(longest, currentTime)

            for nxt, cost in graph.get(node, []):
                if nxt not in shortest:
                    heapq.heappush(pq, (currentTime + cost, nxt))

        return longest if len(shortest) == n else -1