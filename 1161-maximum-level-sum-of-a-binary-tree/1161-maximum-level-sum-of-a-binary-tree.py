class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        currentLevelSum = level = maxLevel = 0
        queue, maxSum = deque([root]), -float('inf')
        while queue:
            level += 1
            levelLength = len(queue)
            for _ in range(levelLength):
                node = queue.popleft()
                currentLevelSum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if currentLevelSum > maxSum:
                maxSum = currentLevelSum
                maxLevel = level
            currentLevelSum = 0
        return maxLevel
