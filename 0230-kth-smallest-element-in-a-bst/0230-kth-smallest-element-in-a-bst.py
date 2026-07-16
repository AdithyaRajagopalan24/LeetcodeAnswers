# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = []
        def dfs(node):
            if node is None:
                return 
            if node.left:
                dfs(node.left)
            inOrder.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return inOrder[k-1]