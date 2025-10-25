class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.bestSum = float("-inf")

        def dfs(node):
            if not node:
                return 0

            leftGain = max(dfs(node.left), 0)
            rightGain = max(dfs(node.right), 0)
            pathSum = node.val + leftGain + rightGain
            self.bestSum = max(self.bestSum, pathSum)
            return node.val + max(leftGain, rightGain)

        dfs(root)
        return self.bestSum
