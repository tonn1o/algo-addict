# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = collections.deque([(root, root.val)])

        while queue:
            (node, sum) = queue.popleft()

            if sum == targetSum and not node.left and not node.right:
                return True

            if node.left:
                queue.append((node.left, sum + node.left.val))

            if node.right:
                queue.append((node.right, sum + node.right.val))

        return False

