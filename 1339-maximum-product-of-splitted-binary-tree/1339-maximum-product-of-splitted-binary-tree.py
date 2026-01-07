class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        allSums = []
        maxVal = 0

        def dfs(node):
            if not node:
                return 0
            currSum = node.val + dfs(node.left) + dfs(node.right)
            allSums.append(currSum)
            return currSum

        totalSum = dfs(root)

        for x in allSums:
            maxVal = max(maxVal, (totalSum - x) * x)

        return maxVal % (10**9 + 7)
