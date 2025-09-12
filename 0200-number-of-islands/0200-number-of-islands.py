class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[-1 for _ in row] for row in grid]
        
        def dfs(x, y):
            visited[x][y] = 1
            directions = [(-1,0), (1,0), (0,1), (0,-1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == "1" and visited[nx][ny] != 1:
                        dfs(nx, ny)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == -1:
                    dfs(i, j)
                    islands += 1
        return islands
