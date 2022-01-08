# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        if not root:
            return 0
        
        def dfs(node, depth):
            nonlocal res
            
            res = max(res, depth)
            
            if node.left:
                dfs(node.left, depth + 1)
                
            if node.right:
                dfs(node.right, depth + 1)
                
        dfs(root, 0)
        return res + 1
                
                            
