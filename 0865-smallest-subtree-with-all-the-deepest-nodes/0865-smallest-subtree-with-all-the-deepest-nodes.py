class Solution:
    maxDepth = 1
    deepestNode = None

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.depthFirstSearch(root, 1)
        return self.deepestNode

    def depthFirstSearch(self, currentNode, currentDepth):
        if not currentNode:
            return currentDepth - 1

        leftDepth = self.depthFirstSearch(currentNode.left, currentDepth + 1)
        rightDepth = self.depthFirstSearch(currentNode.right, currentDepth + 1)

        if leftDepth == rightDepth:
            if leftDepth >= self.maxDepth:
                self.deepestNode = currentNode
                self.maxDepth = leftDepth
            return leftDepth

        return max(leftDepth, rightDepth)
