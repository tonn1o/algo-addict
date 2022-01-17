# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        inorderValIdxMap = dict()

        for i in range(len(inorder)):
            val = inorder[i]
            inorderValIdxMap[val] = i

        preorder_index = 0

        def buildTree(left, right):
            nonlocal preorder_index

            if left > right: return None

            val = preorder[preorder_index]
            root = TreeNode(val)

            preorder_index += 1

            root.left = buildTree(left, inorderValIdxMap[val] - 1)
            root.right = buildTree(inorderValIdxMap[val] + 1, right)

            return root

        return buildTree(0, len(preorder) - 1)
