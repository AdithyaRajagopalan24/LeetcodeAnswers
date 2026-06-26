class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float("-inf")

        def solve(curr):
            if curr is None:
                return 0

            left = max(solve(curr.left), 0)
            right = max(solve(curr.right), 0)

            total = curr.val + left + right
            self.ans = max(self.ans, total)

            return curr.val + max(left, right)

        solve(root)
        return self.ans