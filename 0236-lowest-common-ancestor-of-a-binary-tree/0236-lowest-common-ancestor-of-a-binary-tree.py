class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root in (p, q):
            return root

        leftResult = self.lowestCommonAncestor(root.left, p, q)
        rightResult = self.lowestCommonAncestor(root.right, p, q)

        return root if leftResult and rightResult else leftResult or rightResult