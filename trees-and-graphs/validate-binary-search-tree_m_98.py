# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # bfs
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        queue = collections.deque([(root, -math.inf, math.inf)])

        while queue:
            (node, left_limit, right_limit) = queue.popleft()

            if node.val <= left_limit or node.val >= right_limit:
                return False

            if node.left:
                queue.append((node.left, left_limit, node.val))

            if node.right:
                queue.append((node.right, node.val, right_limit))

        return True


    # dfs
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(node, left_limit, right_limit):
            if not node:
                return True

            if node.val <= left_limit or node.val >= right_limit:
                return False

            return dfs(node.left, left_limit, node.val) and dfs(node.right, node.val, right_limit)

        return dfs(root, -math.inf, math.inf)
