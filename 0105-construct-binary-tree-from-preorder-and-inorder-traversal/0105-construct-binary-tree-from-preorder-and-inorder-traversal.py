class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stk = [root]
        idx = 0

        for val in preorder[1:]:
            cur = TreeNode(val)

            if stk[-1].val != inorder[idx]:
                stk[-1].left = cur
            else:
                while stk and stk[-1].val == inorder[idx]:
                    par = stk.pop()
                    idx += 1
                par.right = cur

            stk.append(cur)

        return root