class Solution:
    def operate_jug(self, action, maxX, maxY, curX, curY):
        if action == "fillx":
            return maxX, curY
        elif action == "filly":
            return curX, maxY
        elif action == "pourx":
            return 0, curY
        elif action == "poury":
            return curX, 0
        elif action == "xy":
            return max(curX - min(maxY - curY, maxX), 0), min(curX + curY, maxY)
        elif action == "yx":
            return min(curX + curY, maxX), max(curY - min(maxX - curX, maxY), 0)
        return 0, 0
        
    def canMeasureWater(self, x, y, target):
        if x + y == target or x == target or y == target:
            return True
        operations = ["fillx", "filly", "pourx", "poury", "yx", "xy"]
        queue = deque([(0, 0)])
        visited = set()
        while queue:
            x1, y1 = queue.popleft()
            if (x1, y1) in visited:
                continue
            if x1 == target or y1 == target or x1 + y1 == target:
                return True
            visited.add((x1, y1))
            for operation in operations:
                next_state = self.operate_jug(operation, x, y, x1, y1)
                queue.append(next_state)
        return False