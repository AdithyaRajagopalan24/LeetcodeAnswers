class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangleRow = [1]
        for i in range(1, rowIndex+1):
            triangleRow.append (int(triangleRow [i-1]*(rowIndex - i + 1)/i))
        return triangleRow