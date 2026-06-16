class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if node is None:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            diameter = max(diameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return diameter