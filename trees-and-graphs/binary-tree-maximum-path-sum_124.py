# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def maxGain(self, node):
            nonlocal maxSum

            if not node:
                return 0

            leftGain = max(self.maxGain(node.left), 0)
            rightGain = max(self.maxGain(node.right), 0)
            maxSum = max(maxSum, leftGain + rightGain + node.val)

            return node.val + max(leftGain, rightGain)

        maxSum = float('-inf')
        maxGain(root)
        return maxSum
