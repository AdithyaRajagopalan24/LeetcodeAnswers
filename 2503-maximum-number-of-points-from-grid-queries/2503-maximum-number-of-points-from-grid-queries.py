class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        result = [0] * len(queries)
        pq = [(grid[0][0], 0, 0)]
        visited.add((0, 0))
        count = 0
        for idx, value in sorted_queries:
            while pq and pq[0][0] < value:
                cell_value, r, c = heapq.heappop(pq)
                count += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        heapq.heappush(pq, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))

            result[idx] = count

        return result