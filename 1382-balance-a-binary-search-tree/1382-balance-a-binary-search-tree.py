class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorderNodes = []

        def inorderTraversal(currentNode):
            if currentNode:
                inorderTraversal(currentNode.left)
                inorderNodes.append(currentNode)
                inorderTraversal(currentNode.right)

        def buildBalancedTree(nodeList):
            if not nodeList:
                return None
            middleIndex = len(nodeList) // 2
            rootNode = nodeList[middleIndex]
            rootNode.left = buildBalancedTree(nodeList[:middleIndex])
            rootNode.right = buildBalancedTree(nodeList[middleIndex + 1:])
            return rootNode

        inorderTraversal(root)
        return buildBalancedTree(inorderNodes)
