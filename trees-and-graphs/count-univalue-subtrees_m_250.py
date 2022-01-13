# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0

        def dfs(node, parentVal):
            nonlocal result

            if not node:
                return True

            if not node.left and not node.right:
                result += 1
                return node.val == parentVal

            isLeftEqual = dfs(node.left, node.val)
            isRightEqual = dfs(node.right, node.val)

            if isLeftEqual and isRightEqual:
                result += 1
                return node.val == parentVal

            return False

        dfs(root, root.val)
        return result
