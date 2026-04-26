class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def findRoot(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findRoot(self.parent[node])
        return self.parent[node]

    def unionNodes(self, nodeA, nodeB):
        rootA = self.findRoot(nodeA)
        rootB = self.findRoot(nodeB)
        if rootA != rootB:
            self.parent[rootA] = rootB
            return False
        return True


class Solution:
    def containsCycle(self, grid):
        rowCount, colCount = len(grid), len(grid[0])
        dsu = DSU(rowCount * colCount)
        
        for row in range(rowCount):
            for col in range(colCount):
                for nextRow, nextCol in [(row, col + 1), (row + 1, col)]:
                    if nextRow < rowCount and nextCol < colCount and grid[row][col] == grid[nextRow][nextCol]:
                        currentIndex = row * colCount + col
                        nextIndex = nextRow * colCount + nextCol
                        
                        if dsu.unionNodes(currentIndex, nextIndex):
                            return True
        return False