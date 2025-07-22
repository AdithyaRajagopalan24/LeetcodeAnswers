# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(node, result):
        if not node:
            return
        inorder(node.left, result)
        result.append(node.val)
        inorder(node.right, result)

    def isSorted(arr):
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False
        return True

    def isValidBST(root):
        result = []
        inorder(root, result)
        return isSorted(result)